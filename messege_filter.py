class MessageFilter:
    def __init__(self, *words):
        self.words = words

    def detect(self, text):
        for word in self.words:
            if word in text:
                return True
        return False
