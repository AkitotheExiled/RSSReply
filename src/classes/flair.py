

class Flair:
    def __init__(self, flair):
        self.flair = flair

    def is_list(self):
        return self.contains_char(",")

    def is_template(self):
        return self.contains_char("-")

    def contains_char(self, char):
        return char in self.get_flair

    def get_flair(self):
        return self.flair

    def to_l(self):
        return self.flair.split(",")

