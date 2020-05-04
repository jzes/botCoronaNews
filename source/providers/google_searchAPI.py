import os
from datetime import date
from models.news import New
import requests
import json


class GoogleSearchAPI:

    BASE_URL = 'https://customsearch.googleapis.com/customsearch/v1'
    date_restricted = ''

    def get_news(self):
        raw_news = self.get_raw_news()

        return list(
            map(
                lambda item: New(item),
                json.loads(raw_news)['items']
            )
        )

    def get_raw_news(self):
        result = requests.get(
            self.BASE_URL,
            params=self.build_search_params(),
            headers=self.build_headers())
        return result.text

    def build_search_params(self):
        date_restricted = date.today()
        return {
            'cx': os.getenv('GOOGLE_CX'),
            'dateRestrict': date_restricted.strftime('%Y-%m-%d'),
            'q': os.getenv('GOOGLE_Q'),
            'key': os.getenv('GOOGLE_API_KEY')
        }

    def build_headers(self):
        return {
            'Accept': 'application/json'
        }
