import json
from newsapi.newsapi_client import NewsApiClient
from newsapi.newsapi_exception import NewsAPIException


class NewsApiSourcesCollector:
    def __init__(self):
        with open('config.json') as f:
            config = json.load(f)
        self.API_KEY = config['NEWS_API_KEY']
        try:
            self.newsapi = NewsApiClient(api_key=self.API_KEY)
            self.sources = self.newsapi.get_sources()
        except NewsAPIException as e:
            print("Invalid API key:", e)

    def export_sources(self):
        if hasattr(self, 'sources'):
            with open('newsapi_sources.json', 'w', encoding='utf8') as f:
                json.dump(self.sources, f, indent=4, ensure_ascii=False)
            print("Exporting was successful")
        else:
            print("Exporting was unsuccessful")


if __name__ == '__main__':
    news = NewsApiSourcesCollector()
    news.export_sources()
