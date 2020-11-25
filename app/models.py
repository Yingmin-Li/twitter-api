
import time

class Tweet:

    id=None
    text=''
    created_at=0
    updated_at=0

    def __init__(self, text):
        self.text=text
        self.created_at="%.20f" % time.time()
        self.updated_at=self.created_at

    def update(self, text):
        self.text=text
        self.updated_at="%.20f" % time.time()

