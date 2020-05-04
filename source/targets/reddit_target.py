import os
import praw
from targets.target import Target

class Reddit(Target):

    def connect(self):
        self.reddit = praw.Reddit(
            client_id=os.getenv('REDDIT_CLIENT_ID'),
            client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
            password=os.getenv('REDDIT_PASSWORD'),
            user_agent=os.getenv('REDDIT_USER_AGENT'),
            username=os.getenv('REDDIT_USER_NAME')
        )
        self.target_r = self.reddit.subreddit(os.getenv('REDDIT_R_TARGET'))

    def post_test(self):
        self.target_r.submit(
            'Test Submit', 'Teste submit body','' ,flair_id=os.getenv('REDDIT_FLAIR_ID')
        )

    def post_new(self, new):
        self.target_r.submit(
            new.title, None ,new.link , flair_id=os.getenv('REDDIT_FLAIR_ID')
        )

    def can_post(self, new)->bool:
        return len(
            list(
                filter(
                    lambda sub: sub.title == new.title,
                    self.get_bot_posts()
                )
            )
        ) == 0

    def get_bot_posts(self):
        return filter(
            lambda sub: sub.link_flair_text == os.getenv('REDDIT_FLAIR_NAME'),
            self.reddit.subreddit('Bauru').new()
        )
        # print(submission.title)
        # print(submission.selftext)
        # print(submission.link_flair_text)
