from dotenv import load_dotenv
from providers.google_searchAPI import GoogleSearchAPI
from targets.reddit_target import Reddit
from targets.twitter_target import Twitter
from service.poster import Poster
from utils.bgcolors import BGColors

class Main:

    def main(self):
        load_dotenv()

        g_search = GoogleSearchAPI()
        news = g_search.get_news()

        twitter = Twitter()
        reddit = Reddit()
        
        poster = Poster()
        print(BGColors.OKGREEN+'===Reddit target run==='+BGColors.ENDC)
        poster.run_poster(reddit, news)
        print(BGColors.OKGREEN+'===Twitter target run==='+BGColors.ENDC)
        poster.run_poster(twitter, news)    


if __name__ == "__main__":
    main = Main()
    main.main()
