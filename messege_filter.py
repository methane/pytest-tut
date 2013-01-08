class MessageFilter:
    def __init__(self, word):
        self.word = word

    def detect(self, text):
        return self.word in text
