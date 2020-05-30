import argparse
import logging
from time import sleep

from config import create_api  # TODO: Resolve the pycharm issue to import local module
import tweepy

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Create the CLI parser
keywords_parser = argparse.ArgumentParser(
    prog='like_retweet.py',
    description='Get the list of keywords to focus on in the twitter stream',
    fromfile_prefix_chars='@'
)

# TODO: Make the parser getting a list of keywords from the 'cli-args.txt' file
keywords_parser.add_argument('arg_1', help='a first argument')
keywords_parser.add_argument('arg_2', help='a second argument')
keywords_parser.add_argument('arg_3', help='a third argument')
keywords_parser.add_argument('arg_4', help='a fourth argument')
keywords_parser.add_argument('arg_5', help='a fifth argument')
keywords_parser.add_argument('arg_6', help='a sixth argument')
keywords_parser.add_argument('arg_7', help='a seventh argument')
keywords_parser.add_argument('arg_8', help='a eighth argument')
keywords_parser.add_argument('arg_9', help='a ninth argument')
keywords_parser.add_argument('arg_10', help='a tenth argument')
keywords_parser.add_argument('arg_11', help='a eleventh argument')


class LikeRetweetListener(tweepy.StreamListener):
    """
    The stream listener class which allows to receive tweets from the stream.
    """
    def __init__(self, api):
        super().__init__(api)
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        """
        Like and Retweet tweets from the stream which matches filtering criteria applied by the stream object.
        :param tweet: a given tweet from the stream
        """
        logger.info(f"processing tweet id {tweet.id}")

        if tweet.in_reply_to_status_id is not None or tweet.user.id == self.me.id:
            # Ignore my own tweets
            return

        if not tweet.favorited:
            # Mark tweet as liked if it's not done yet
            try:
                tweet.favorite()
            except tweepy.TweepError as e:
                logger.warning(e.reason)
            sleep(5)

        if not tweet.retweeted:
            # Retweet it if it's not done yet
            try:
                tweet.retweet()
            except tweepy.TweepError as e:
                logger.warning(e.reason)
            sleep(5)

    def on_error(self, tweet):
        """
        Errors logging
        :param tweet: a given tweet from the stream
        """
        logger.error(tweet)


def main(keywords):
    api = create_api()
    tweets_listener = LikeRetweetListener(api)
    stream = tweepy.Stream(auth=api.auth, listener=tweets_listener)
    stream.filter(track=keywords, languages=['fr'])


if __name__ == '__main__':
    args = keywords_parser.parse_args()
    keywords = list(vars(args).values())
    main(keywords)
