import json
import requests

from stock_price_database import StockPriceDataBase

class StockPriceDataCollector:
    def __init__(self):
        with open('config.json') as f:
            config = json.load(f)
        self.API_KEY = config['ALPHA_API_KEY']

        self.STOCKS = config['stocks']

    def get_data(self, stock):
        # info: https://www.alphavantage.co/documentation/
        # WARN: API call frequency is 5 calls per minute and 500 calls per day.
        if stock not in self.STOCKS:
            raise ValueError('Unknown stock:', stock)

        result = requests.get(
            f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={self.STOCKS[stock]}&interval=1min&outputsize=full&apikey={self.API_KEY}')
        db = StockPriceDataBase(result)
        return db.database
