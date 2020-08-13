from configparser import ConfigParser
from src.database.database import Database
from src.classes.logger import Logger
import os

temp_path = os.path.dirname(os.path.abspath(__file__))
config = os.path.join(temp_path, "../../config.ini")
print(config)
FEEDTYPE = {"latest": 1, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "all": 10000}

def get_int(possible_integer):
    try:
        my_int = int(possible_integer)
    except ValueError:
        my_int = FEEDTYPE.get(possible_integer.lower(), 3)
    finally:
        return my_int



class RedditBaseClass:

    def __init__(self):
        try:
            self.CONFIG = ConfigParser()
            self.CONFIG.read(config)
        # Retrieving User information from config.ini for PRAW
            self.user = self.CONFIG.get('main', 'USER')
            self.password = self.CONFIG.get('main', 'PASSWORD')
            self.client = self.CONFIG.get('main', 'CLIENT_ID')
            self.secret = self.CONFIG.get('main', 'SECRET')
            self.delay = self.CONFIG.getint('main', 'DELAY')
            self.subreddit = self.CONFIG.get('main', 'SUBREDDIT')
            self.rss_url = self.CONFIG.get('main', 'RSSURL')
            self.run_once = self.CONFIG.getboolean('main', 'RUN_ONCE')
            self.count = get_int(self.CONFIG.get('main', 'FEED_TYPE'))
            self.log = Logger()
            self.logger = self.log.logger
        except Exception:
            self.logger.info(f"ERROR RETRIEVING CONFIG: {config}", exc_info=True)

