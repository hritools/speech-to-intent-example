from typing import List

from newsapi import NewsApiClient


API_KEY = '1412455323e8485b89be90122053e3a5'


def get_headlines(category :str =None) -> List[str]:
    try:
        api = NewsApiClient(API_KEY)
        news = api.get_top_headlines(language='ru', country='ru', page_size=5, category=category)
        headlines = [article['title'] for article in news['articles']]
        return headlines
    except Exception:
        return []