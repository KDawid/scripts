import datetime


class StockPriceDataItem:
    def __init__(self, date_time_str):
        self.date = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')

    def get_tuple(self):
        return self.date, self.open, self.high, self.low, self.close, self.volume


class AlphavantageStockPriceDataItem(StockPriceDataItem):
    def __init__(self, date_time_str, data_item):
        StockPriceDataItem.__init__(self, date_time_str)
        self.open = float(data_item.get('1. open'))
        self.high = float(data_item.get('2. high'))
        self.low = float(data_item.get('3. low'))
        self.close = float(data_item.get('4. close'))
        self.volume = float(data_item.get('5. volume'))


class YfinanceStockPriceDataItem(StockPriceDataItem):
    def __init__(self, date_time_str, data_item):
        StockPriceDataItem.__init__(self, date_time_str)
        self.open = float(data_item.get('Open'))
        self.high = float(data_item.get('High'))
        self.low = float(data_item.get('Low'))
        self.close = float(data_item.get('Close'))
        self.volume = float(data_item.get('Volume'))
