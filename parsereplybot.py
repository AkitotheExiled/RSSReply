import praw
from praw.exceptions import APIException, RedditAPIException
import os
import requests, requests.auth
from src.classes.baseclass import RedditBaseClass
from src.database.database import Articles, Database
from src.classes.logger import Logger
import time, static
from rssparse import get_links_titles_guuids



SCRIPT_DIR = os.path.dirname(__file__)



class Parse_Reply_Bot(RedditBaseClass):


    def __init__(self):
        super().__init__()
        self.user_agent = "PC:ParseNReply :V1.21 by ScoopJr"
        if self.devmode:
            print("DEVMODE ENABLED",self.user_agent)
        else:
            print(self.user_agent)
        self.reddit = praw.Reddit(client_id=self.client,
                                  client_secret=self.secret,
                                  password=self.password,
                                  user_agent=self.user_agent,
                                  username=self.user)
        self.reddit.validate_on_submit = True
        self.queue = {"data": []}
        self.db = Database()
        self.error_delay = 140
        self.photo_dir = SCRIPT_DIR +  "/src/temp_photos/"
        print(self.photo_dir)
        self.images_to_delete = []
        self.resubmit = True



    def check_for_database(self):
        for file in os.listdir(os.getcwd()):
            if static.DATABASE_NAME in file:
                return True
        return False
    
    def exist_check_or_add_posts(self, model, **kwargs):
        instance = self.db.session.query(model).filter_by(**kwargs).first()
        if instance:
            print(instance)
            return True
        else:
            try:
                instance = model(**kwargs)
                self.db.session.add(instance)
                self.db.session.commit()
                self.delay = self.defaultdelay
                return False
            except Exception as e:
                self.logger.error(e + "Error getting data from rss feed", exc_info=True)

    def exist_check_and_dont_add(self, model, **kwargs):
        instance = self.db.session.query(model).filter_by(**kwargs).first()
        if instance:
            return True
        else:
            return False

    def get_text_from_rssfeed(self, url):
        headers = {'User-Agent': self.user_agent}
        try:
            while True:
                print("Attempting to get rss feed info...")
                data = requests.get(url, headers=headers)
                if data.status_code == requests.codes.ok:
                    if data:
                        return data.text
                    else:
                        time.sleep(self.delay)
        except Exception:
            self.logger.error("Error getting data from rss feed", exc_info=True)

    def sort_and_exist_check_posts(self, data):
        for item in data["data"]:
            link = item["link"]
            title = item["title"]
            desc = item["desc"]
            if self.prefer_images:
                images = self.save_replace_external_images_locally(item["images"])
            else:
                images = []
            title_exist = self.exist_check_and_dont_add(Articles, link=item["link"])

            if title_exist:
                print(f"Article Exists? -> {title_exist}. Skipping to the next article. . .")
                return False
            else:
                self.exist_check_or_add_posts(Articles, id=item["id"],
                                              title=item["title"],
                                              link=item["link"])
                return {"title": title, "link": link, "desc": desc, "images": images}

    def handle_post_logic(self, item, sub, flairid=None):
        if flairid is not None:
            print(
                f"Article: ({item['title']}, {item['link']}) posted in {sub} with {flairid}")
            if item['images']:
                if len(item['images']) > 1:
                    submission = self.reddit.subreddit(sub).submit_gallery(item['title'],
                                                                           images=item[
                                                                               'images'],
                                                                           flair_id=flairid)
                elif len(item['images']) < 2 and len(item['images']) > 0:
                    submission = self.reddit.subreddit(sub).submit_image(item['title'],
                                                                         image_path=
                                                                         item['images'][0][
                                                                             'image_path'],
                                                                         resubmit=self.resubmit,
                                                                         flair_id=flairid)
            else:
                try:
                    if self.prefer_desc:
                        submission = self.reddit.subreddit(sub).submit(item['title'],
                                                                       selftext=item['desc'],
                                                                       resubmit=self.resubmit,
                                                                       flair_id=flairid)
                    else:
                        submission = self.reddit.subreddit(sub).submit(item['title'],
                                                                       url=item['link'],
                                                                       resubmit=self.resubmit,
                                                                       flair_id=flairid)
                        if self.comment_desc and len(item['desc']) >= 1 and not self.prefer_desc:
                            submission.reply(body=item['desc'])
                        if self.reddit.subreddit(sub).user_is_moderator:
                            submission.mod.approve()
                except RedditAPIException as exc:
                    if not str(exc).startswith('ALREADY_SUB'):
                        raise
                    else:
                        self.exist_check_or_add_posts(Articles, id=item["id"],
                                                      title=item["title"],
                                                      link=item["link"])


        else:
            print(
                f"Article: ({item['title']}, {item['link']}) posted in {sub} without {flairid}")
            if item['images']:
                if len(item['images']) > 1:
                    submission = self.reddit.subreddit(sub).submit_gallery(item["title"],
                                                                           images=item[
                                                                               'images'])
                    if self.comment_desc and len(item['desc']) >= 1:
                        submission.reply(body=item['desc'])
                elif len(item['images']) < 2 and len(item['images']) > 0:
                    submission = self.reddit.subreddit(sub).submit_image(item["title"],
                                                                     image_path=
                                                                     item['images'][0][
                                                                         'image_path'],
                                                                     resubmit=self.resubmit)
                    if self.comment_desc and len(item['desc']) >= 1:
                        submission.reply(body=item['desc'])
            else:
                if self.prefer_desc:
                    submission = self.reddit.subreddit(sub).submit(item['title'],
                                                                   selftext=item['desc'],
                                                                   resubmit=self.resubmit,
                                                                   flair_id=flairid)
                else:
                    submission = self.reddit.subreddit(sub).submit(item["title"],
                                                                   url=item["link"],
                                                                   resubmit=self.resubmit)
                    if self.comment_desc and len(item['desc']) >= 1:
                        submission.reply(body=item['desc'])
                if self.reddit.subreddit(sub).user_is_moderator:
                    submission.mod.approve()
                    if flairid is not None:
                        submission.mod.flair(flair_template_id=flairid)


    def run_loop(self):
        while True:
            for subart in self.subrss:
                sub = subart["subreddit"]
                rssurl = subart["rssurl"]
                flairid = subart["flair"]
                url_count = 0
                for url in rssurl.get_url():
                    print(url)
                    self.delete_temp_images()
                    rss_text = self.get_text_from_rssfeed(url)
                    if rss_text:
                        data = get_links_titles_guuids(text=rss_text)

                        if data:
                            item = self.sort_and_exist_check_posts(data)
                            if not item:
                                continue
                            else:
                                while True:
                                    if len(flairid) > 1:
                                        try:
                                            self.handle_post_logic(item, sub, flairid=flairid[url_count])
                                            break
                                        except (APIException, RedditAPIException):
                                            self.logger.error("Error has occurred within the API", exc_info=True)
                                            time.sleep(self.error_delay)
                                    else:
                                        try:
                                            self.handle_post_logic(item, sub, flairid=flairid)
                                            break
                                        except (APIException, RedditAPIException):
                                            self.logger.error("Error has occurred within the API", exc_info=True)
                                            time.sleep(self.error_delay)

                    url_count += 1
                if self.run_once:
                    break
                else:
                    print(f"Waiting {self.delay} seconds before attempting to pull next subreddit/article.")
                    time.sleep(self.delay)
    def main(self):
       self.run_loop()


    def save_replace_external_images_locally(self, ext_images):
        local_imgs = []
        save_location = "/src/temp_photos/"

        for ext_img in ext_images:
            src = ext_img['image_path']
            local_save_path = f'{SCRIPT_DIR}' + f'{save_location}' + src.rsplit('/', 1)[-1]

            with open(local_save_path, 'wb') as f:
                f.write(requests.get(src).content)
                f.close()
            self.images_to_delete.append(local_save_path)
            local_imgs.append({'image_path': local_save_path})
        return local_imgs

    def delete_temp_images(self):
        for img in os.scandir(self.photo_dir):
            os.remove(img.path)

if __name__ == '__main__':
    bot = Parse_Reply_Bot()
    bot.main()