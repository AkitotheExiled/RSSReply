

class Flair:
    def __init__(self, flair):
        self.flair = flair.split(",")
        self.length = self.length()

    def is_list(self):
        return self.contains_char(",")

    def is_template(self):
        return self.contains_char("-")

    def is_none(self):
        return self.contains_char("None")

    def contains_char(self, char):
        return all(list(char in word for word in self.get_flair()))

    def get_flair(self):
        return self.flair

    def to_l(self):
        return self.flair.split(",")

    def length(self):
        return len(self.flair)


