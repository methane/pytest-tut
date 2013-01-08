class MessageFilter:
    def __init__(self, *words):
        self.ng_words = set(words)

    def detect(self, text):
        return any(word in text for word in self.ng_words)
