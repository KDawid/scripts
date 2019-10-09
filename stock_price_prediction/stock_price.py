import argparse
import csv
import json
import logging
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
        logging.basicConfig(filename='logfile.log', level=logging.INFO, format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %H:%M:%S')


    def save(self):
        logging.info('Saving stock price data...')
        for stock in self.STOCKS:
            self.__save_stock(stock)
        logging.info('Saving stock price data has finished.')

    def export(self):
        logging.info(f'Exporting stock price data...')
        self.__clean_exported_data()
        for stock in self.STOCKS:
            self.__export_stock(stock)
        try:
            subprocess.run(["tar", "-czvf", f"{self.EXPORT_TAR}", f"{self.EXPORT_FOLDER}"])
            logging.info('Exporting stock price data has finished.')
        except subprocess.CalledProcessError as e:
            logging.error(f'Export failed: {e}')
        self.__remove_export_folder()

    def __save_stock(self, stock):
        logging.debug(f'Saving data for {stock}')
        self.saver.save(stock)
        logging.debug(f'Sleep {self.sleep_time} seconds to avoid API overloading...')
        time.sleep(self.sleep_time)

    def __export_stock(self, stock):
        with open(f'{self.EXPORT_FOLDER}/{stock}.csv', 'w') as f:
            csv_out = csv.writer(f)
            for item in self.saver.export(stock):
                csv_out.writerow(item)

    def __clean_exported_data(self):
        self.__remove_tar()
        self.__remove_export_folder()
        os.mkdir(self.EXPORT_FOLDER)

    def __remove_tar(self):
        if os.path.exists(f"{self.EXPORT_TAR}"):
            os.remove(f"{self.EXPORT_TAR}")

    def __remove_export_folder(self):
        if os.path.exists(self.EXPORT_FOLDER):
            shutil.rmtree(self.EXPORT_FOLDER)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Manage stock price data')
    parser.add_argument('-s', '--save', action='store_true', help='Save new stock price data from API')
    parser.add_argument('-e', '--export', action='store_true', help='Export stock price data')
    args = parser.parse_args()
    main = Main()
    if args.save:
        main.save()
    if args.export:
        main.export()
