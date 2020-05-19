import json
import requests
import yfinance as yf

from stock_price_database import AlphavantageStockPriceDataBase
from stock_price_database import YfinanceStockPriceDataBase


class StockPriceDataCollector:
    def get_data(self, stock):
        raise NotImplementedError("Stock Price Data Cololector should be implemented!")


class AlphavantageStockPriceDataCollector(StockPriceDataCollector):
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
        db = AlphavantageStockPriceDataBase(result)
        return db.database

class YfinanceStockPriceDataCollector(StockPriceDataCollector):
    def __init__(self):
        with open('config.json') as f:
            config = json.load(f)
        self.STOCKS = config['stocks']

    def get_data(self, stock):
        if stock not in self.STOCKS:
            raise ValueError('Unknown stock:', stock)

        data = yf.download(tickers=self.STOCKS[stock], period='7d', interval="1m")
        db = YfinanceStockPriceDataBase(data)
        return db.database
