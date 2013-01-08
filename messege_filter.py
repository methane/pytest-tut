class MessageFilter:
    def __init__(self, *words):
        self.words = words

    def detect(self, text):
        return any(word in text for word in self.words)
