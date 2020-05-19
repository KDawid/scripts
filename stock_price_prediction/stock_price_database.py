import json
import logging
import matplotlib.pyplot as plt

from stock_price_data_item import AlphavantageStockPriceDataItem
from stock_price_data_item import YfinanceStockPriceDataItem

class StockPriceDataBase:
    def __init__(self, request):
        logging.basicConfig(filename='logfile.log',
                            level=logging.INFO,
                            format='%(asctime)s [%(filename)s:%(lineno)s] %(message)s',
                            datefmt='%m/%d/%Y %H:%M:%S')
        self.database = set()
        self.meta_data = None
        self.update_data(request)

    def update_data(self, request):
        raise NotImplementedError("Stock Price Database should be implemented")


class AlphavantageStockPriceDataBase(StockPriceDataBase):
    def __init__(self, request):
        StockPriceDataBase.__init__(self, request)

    def update_data(self, request):
        try:
            data = json.loads(request.text)
            self.meta_data = data['Meta Data']

            data_temp = data['Time Series (1min)']
            for date_time, data_item in data_temp.items():
                item = AlphavantageStockPriceDataItem(date_time, data_item)
                self.database.add(item)
        except:
            logging.error(f'Could not parse data from result: {request.text}')

    def plot(self, start_date, end_date):
        start = datetime.datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
        end = datetime.datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')

        plt.figure(figsize=(10, 5))
        open_price = []
        high_price = []
        low_price = []
        close_price = []
        dates = []
        for item in sorted(self.database, key=lambda x: x.date):
            if not start <= item.date <= end:
                continue
            open_price.append(item.open)
            high_price.append(item.high)
            low_price.append(item.low)
            close_price.append(item.close)
            dates.append(item.date)

        plt.plot(open_price)
        plt.plot(high_price)
        plt.plot(low_price)
        plt.plot(close_price)

        plt.legend(['open', 'high', 'low', 'close'])
        plt.title(f'Stock prices of {self.meta_data["2. Symbol"]} between {start_date} and {end_date}')
        plt.show()


class YfinanceStockPriceDataBase(StockPriceDataBase):
    def __init__(self, request):
        StockPriceDataBase.__init__(self, request)

    def update_data(self, request):
        try:
            data = request.to_dict(orient='index')
            for date_time, data_item in data.items():
                item = YfinanceStockPriceDataItem(str(date_time)[:-6], data_item)
                self.database.add(item)
        except:
            logging.error(f'Could not parse data from result: {request[:100]}')
