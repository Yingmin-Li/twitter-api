from unittest import TestCase
from app.models import Tweet, TweetRepository  # We will code our `repo` class in `app/models.py`

class TestTweetRepository(TestCase):

    def test_instance_variables(self):
        # Create an instance of the `repo` class with one argument
        repo = TweetRepository()
        # Check that `text` holds the content of the repo
        self.assertEqual(repo.tweets_count(), 0)

    def test_new_tweet(self):
        repo = TweetRepository()
        old_size = repo.tweets_count()

        tweet = Tweet("my first tweet")
        self.assertIsNotNone(tweet.created_at)
        new_tweet = repo.add(tweet)
        self.assertIsNotNone(new_tweet.id)

        new_size = repo.tweets_count()

        self.assertEqual(old_size+1, new_size)

    def test_del_tweet(self):
        repo = TweetRepository()
        tweet = Tweet("my first tweet")
        new_tweet = repo.add(tweet)
        old_size = repo.tweets_count()

        tweet = repo.del_tweet(1)
        self.assertIsNotNone(tweet.id)

        new_size = repo.tweets_count()

        self.assertEqual(old_size-1, new_size)
