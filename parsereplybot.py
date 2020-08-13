import praw
from praw.exceptions import APIException
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
        self.user_agent = "PC:ParseNReply :V1.03 by ScoopJr"
        print('Starting up...', self.user_agent)
        self.reddit = praw.Reddit(client_id=self.client,
                                  client_secret=self.secret,
                                  password=self.password,
                                  user_agent=self.user_agent,
                                  username=self.user)
        self.reddit.validate_on_submit = True
        self.queue = {"data": []}
        self.db = Database()
        self.log = Logger()
        self.logger = self.log.logger
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
                return False
            except Exception as e:
                print(e)

    def exist_check_and_dont_add(self, model, **kwargs):
        instance = self.db.session.query(model).filter_by(**kwargs).first()
        if instance:
            print(instance)
            return True
        else:
            return False

    def get_text_from_rssfeed(self):
        url = "https://n4g.com/rss/news?channel=next-gen&sort=latest"
        headers = {'User-Agent': self.user_agent}
        try:
            while True:
                print("Attempting to get rss feed info...")
                data = requests.get(self.rss_url, headers=headers)
                if data.status_code == requests.codes.ok:
                    if data:
                        return data.text
                    else:
                        time.sleep(self.delay)
        except Exception:
            self.logger.info("Error getting data from rss feed", exc_info=True)


    def main(self):
        while True:
            print(f"Getting RSS Feed... from {self.rss_url}")
            rss_text = self.get_text_from_rssfeed()
            if rss_text:
                data = get_links_titles_guuids(text=rss_text)
                if data:
                    for item in data["data"]:
                        link = item["link"]
                        title = item["title"]
                        title_exist = self.exist_check_and_dont_add(Articles, title=item["title"])
                        if title_exist:
                            continue
                        else:
                            does_exist = self.exist_check_or_add_posts(Articles, id=item["id"], title=item["title"],
                                                                   link=item["link"])
                            if not does_exist:
                                while True:
                                    try:
                                        self.reddit.subreddit(self.subreddit).submit(title, url=link)
                                        print(f"Posting in {self.subreddit}, title: {item['title']}")
                                        break
                                    except APIException as exception:
                                        self.logger.info("Error has occurred within the API", exc_info=True)
                                        time.sleep(self.error_delay)
                                        pass
                            else:
                                print(f"Title: {item['title']} already exists in {self.subreddit}. Continuing...")
            if self.run_once:
                break
            else:
                print(f"Waiting {self.delay} seconds before attempting to pull another article.")
                time.sleep(self.delay)



if __name__ == '__main__':
    bot = Parse_Reply_Bot()
    bot.main()