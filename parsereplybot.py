import praw
from praw.exceptions import APIException, RedditAPIException
import os
import requests, requests.auth
from src.classes.baseclass import RedditBaseClass
from src.database.database import Articles, Database
from src.classes.logger import Logger
import time, static
from rssparse import get_links_titles_guuids






class Parse_Reply_Bot(RedditBaseClass):

    def __init__(self):
        super().__init__()
        self.user_agent = "PC:ParseNReply :V1.06 by ScoopJr"
        print('Starting up...', self.user_agent)
        self.reddit = praw.Reddit(client_id=self.client,
                                  client_secret=self.secret,
                                  password=self.password,
                                  user_agent=self.user_agent,
                                  username=self.user)
        self.reddit.validate_on_submit = True
        self.queue = {"data": []}
        self.db = Database()
        self.error_delay = 140


    def get_token(self):
        """ Retrieves token for Reddit API."""
        client_auth = requests.auth.HTTPBasicAuth(self.client, self.secret)
        post_data = {'grant_type': 'password', 'username': self.user, 'password': self.password}
        headers = {'User-Agent': self.user_agent}
        response = requests.Session()
        response2 = response.post(self.token_url, auth=client_auth, data=post_data, headers=headers)
        self.token = response2.json()['access_token']
        self.t_type = response2.json()['token_type']

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
                self.logger.error("Error getting data from rss feed", exc_info=True)

    def exist_check_and_dont_add(self, model, **kwargs):
        instance = self.db.session.query(model).filter_by(**kwargs).first()
        if instance:
            self.delay+=10
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


    def main(self):
        while True:
            for subart in self.subrss:
                sub = subart["subreddit"]
                rssurl = subart["rssurl"]
                flairid = subart["flair"]
                print(f"Getting RSS Feed... from {rssurl}")
                for url in rssurl.get_url():
                    rss_text = self.get_text_from_rssfeed(url)
                    if rss_text:
                        data = get_links_titles_guuids(text=rss_text)
                        if data:
                            i = 0
                            for item in data["data"]:
                                if i == self.count:
                                    break
                                link = item["link"]
                                title = item["title"]
                                title_exist = self.exist_check_and_dont_add(Articles, title=item["title"])
                                i+=1
                                if title_exist:
                                    print(f"Article: {title}, already exists in the database/subreddit!")
                                    continue
                                else:
                                    does_exist = self.exist_check_or_add_posts(Articles, id=item["id"], title=item["title"],
                                                                           link=item["link"])
                                    if not does_exist:
                                        while True:
                                            try:
                                                submission = self.reddit.subreddit(sub).submit(title, url=link, resubmit=False)
                                                if self.reddit.subreddit(sub).user_is_moderator:
                                                    submission.mod.approve()
                                                    if flairid is not None:
                                                        submission.mod.flair(flair_template_id=flairid)
                                                print(f"Posting in {sub}, title: {item['title']}")
                                                break
                                            except (APIException, RedditAPIException):
                                                self.logger.error("Error has occurred within the API", exc_info=True)
                                                time.sleep(self.error_delay)
                                                break
                                    else:
                                        print(f"Title: {item['title']} already exists in {sub}. Continuing...")
                if self.run_once:
                    break
                else:
                    print(f"Waiting {self.delay} seconds before attempting to pull next subreddit/article.")
                    time.sleep(self.delay)



if __name__ == '__main__':
    bot = Parse_Reply_Bot()
    bot.main()