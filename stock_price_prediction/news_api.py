from newsapi.newsapi_client import NewsApiClient

with open('config.json') as f:
    config = json.load(f)

API_KEY = config['NEWS_API_KEY']

# Init
newsapi = NewsApiClient(api_key=API_KEY)

all_articles = newsapi.get_everything(q='apple',
                                      sources='bloomberg,reuters',
                                      from_param='2019-10-07',
                                      to='2019-11-07',
                                      language='en')
print(all_articles)
print()
