import time

from stock_price_saver import StockPriceSaver

class Main:
    def __init__(self):
        self.sleep_time = 15
        self.STOCKS = {'apple': 'AAPL',
                       'microsoft': 'MFST',
                       'facebook': 'FB',
                       'ibm': 'IBM',
                       'ericsson': 'ERIC',
                       'sony': 'SNE'
                       }

    def run(self):
        for stock in self.STOCKS:
            print(f'Saving data for {stock}')
            saver = StockPriceSaver(stock)
            saver.save()
            print(f'Sleep {self.sleep_time} seconds to avoid API overloading...')
            time.sleep(self.sleep_time)


if __name__ == '__main__':
    main = Main()
    main.run()
