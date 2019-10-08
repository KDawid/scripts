import csv
import json
import os
import shutil
import subprocess
import time

from stock_price_saver import StockPriceSaver


class Main:
    def __init__(self):
        self.saver = StockPriceSaver()
        with open('config.json') as f:
            config = json.load(f)
        self.STOCKS = config['stocks'].keys()
        self.EXPORT_FOLDER = config['export_folder']
        self.EXPORT_TAR = config['export_tar']
        self.sleep_time = 15


    def save(self):
        for stock in self.STOCKS:
            print(f'Saving data for {stock}')

            self.saver.save(stock)
            print(f'Sleep {self.sleep_time} seconds to avoid API overloading...')
            time.sleep(self.sleep_time)

    def export(self):
        print(f'Export data')
        self.__clean_exported_data()
        for stock in self.STOCKS:
            with open(f'{self.EXPORT_FOLDER}/{stock}.csv', 'w') as f:
                csv_out = csv.writer(f)
                for item in self.saver.export(stock):
                    csv_out.writerow(item)
        subprocess.run(["tar", "-czvf", f"{self.EXPORT_TAR}", f"{self.EXPORT_FOLDER}"])

    def __clean_exported_data(self):
        if os.path.exists(f"{self.EXPORT_TAR}"):
            os.remove(f"{self.EXPORT_TAR}")
        if os.path.exists(self.EXPORT_FOLDER):
            shutil.rmtree(self.EXPORT_FOLDER)
        os.mkdir(self.EXPORT_FOLDER)


if __name__ == '__main__':
    main = Main()
    main.save()
    main.export()
