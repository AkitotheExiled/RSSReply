import json
class Rssurl:
    def __init__(self, rssurl):
        self.url = rssurl.split(",")

    def is_list(self):
        return type(self.url) == type(list)

    def contains_char(self, char):
        return char in self.get_url

    def get_url(self):
        return self.url
