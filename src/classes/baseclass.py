from configparser import ConfigParser
from configparser import NoSectionError
from src.database.database import Database
from src.classes.logger import Logger
import os, sys

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
        log = Logger()
        self.logger = log.log
        try:
            self.CONFIG = ConfigParser()
            self.CONFIG.read(config)
        # Retrieving User information from config.ini for PRAW
            self.user = self.CONFIG.get('main', 'USER')
            self.password = self.CONFIG.get('main', 'PASSWORD')
            self.client = self.CONFIG.get('main', 'CLIENT_ID')
            self.secret = self.CONFIG.get('main', 'SECRET')
            self.delay = self.CONFIG.getint('main', 'DELAY')
            self.defaultdelay = self.CONFIG.getint('main', 'DELAY')
            self.run_once = self.CONFIG.getboolean('main', 'RUN_ONCE')
            self.count = get_int(self.CONFIG.get('main', 'FEED_TYPE'))
            self.subrss = []
            try:
                for k,v in self.CONFIG.items('suburl'):
                    self.subrss.append({"subreddit": k, "rssurl": v})
            except NoSectionError as e:
                self.logger.error("Section: ['suburl'] could not be found!  Please check your config.ini file!", exc_info=True)
                raise Exception("Section: ['suburl'] could not be found!  Please check your config.ini file!") from e
        except Exception:
            self.logger.warning("[GENERAL ERROR] An issue occurred when attempting to retrieve info from config.ini.  Check all error messages!", exc_info=True)
            sys.exit(1)

