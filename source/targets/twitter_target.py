import twitter
import os
from targets.target import Target


class Twitter(Target):

    def connect(self):
        self.api = twitter.Api(consumer_key=os.getenv('TWITTER_CONSUMER_KEY'),
                  consumer_secret=os.getenv('TWITTER_CONSUMER_SECRET'),
                  access_token_key=os.getenv('TWITTER_ACCESS_TOKEN_KEY'),
                  access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))
    
    def post_new(self, new):
        self.api.PostUpdate(self.build_tweet_from_new(new))

    def can_post(self, new)->bool:
        return len(
            list(
                filter(
                    lambda post: post.split('\n')[0] == new.title,
                    self.get_bot_posts()
                )
            )
        ) == 0
        

    def get_bot_posts(self):
        tweets = self.api.GetUserTimeline(screen_name=os.getenv('TWITTER_SCREEN_NAME'))
        return [tweet.text for tweet in tweets]
        

    def build_tweet_from_new(self, new):
        return new.title+'\n'+new.body+'\n'+new.link
