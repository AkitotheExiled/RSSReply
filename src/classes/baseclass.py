from configparser import ConfigParser
from configparser import NoSectionError, NoOptionError
from src.classes.flair import Flair
from src.classes.rssurl import Rssurl
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
            self.CONFIG = ConfigParser(defaults=None, interpolation=None)
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
                self.flairids = Flair(self.CONFIG.get('flairs', 'FLAIR_IDS'))
            except NoOptionError:
                self.logger.warning("Flair section could not be found! Script will continue without flairs.",
                                  exc_info=True)
                self.flairids = None
            try:
                for k,v in self.CONFIG.items('suburl'):
                    rssurl = Rssurl(v)
                    self.subrss.append({"subreddit": k, "rssurl": rssurl, "flair": None})
            except NoSectionError as e:
                self.logger.error("Section: ['suburl'] could not be found!  Please check your config.ini file!", exc_info=True)
                raise Exception("Section: ['suburl'] could not be found!  Please check your config.ini file!") from e
            if self.flairids is not None:
                if not self.flairids.is_template():
                    raise Exception("You need to use a flair template id!  I.E. 8923hdnd-3829493f-1383eh28 and not a flair name!")
                if self.flairids.is_list():
                    self.flairids = self.flairids.to_l()
                    if len(self.flairids) != len(self.subrss):
                        raise Exception("Your subreddits/feeds amount does not match your flairids amount.")
                    else:
                        for item, flair in zip(self.subrss, self.flairids):
                            item["flair"] = flair
                print(self.subrss)
        except Exception:
            self.logger.warning("[GENERAL ERROR] An issue occurred when attempting to retrieve info from config.ini.  Check all error messages!", exc_info=True)
            sys.exit(1)

