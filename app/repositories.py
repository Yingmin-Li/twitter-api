from .models import Tweet
import itertools

class TweetRepository:

    tweets=[]

    def __init__(self):
        pass

    def clear(self):
       tweets=[]

    def add(self, tweet):
        tweet.id=self.next_id() # generate tweet id
        self.tweets.append(tweet)
        return tweet

    def tweets_count(self):
        return len(self.tweets)

    def get(self, id):
        if id > len(self.tweets):
            return None
        tweet=self.tweets[id-1]
        if tweet is None:
            return None
        return tweet


    def next_id(self):
        START_INDEX = len(self.tweets) + 1
        IDENTIFIER_GENERATOR = itertools.count(START_INDEX)
        return next(IDENTIFIER_GENERATOR)

    def del_tweet(self, id):
        tweet=self.tweets[id-1]
        if tweet is None:
            return None

        self.tweets.pop(id-1)
        return tweet

    def update_tweet(self, id, text):
        tweet=self.tweets[id-1]

        if tweet is None:
            return None

        tweet.update(text)

        for key in range(len(self.tweets)):
            if key == id -1 :
                self.tweets[key]=tweet

        return self.tweets[id-1]

