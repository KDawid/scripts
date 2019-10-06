import datetime

class StockPriceDataItem:
    def __init__(self, date_time_str, data_item):
        self.date = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
        self.open = float(data_item.get('1. open'))
        self.high = float(data_item.get('2. high'))
        self.low = float(data_item.get('3. low'))
        self.close = float(data_item.get('4. close'))
        self.volume = float(data_item.get('5. volume'))

    def get_tuple(self):
        return self.date, self.open, self.high, self.low, self.close, self.volume