from providers.google_searchAPI import GoogleSearchAPI

class Main:

    def main(self):

        g_search = GoogleSearchAPI()
        news = g_search.get_news()   


if __name__ == "__main__":
    main = Main()
    main.main()
