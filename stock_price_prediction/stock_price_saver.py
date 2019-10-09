import json
import logging
import pymysql as dbapi

from pymysql.err import IntegrityError
from stock_price_data_collector import StockPriceDataCollector


class StockPriceSaver:
    def __init__(self):
        with open('config.json') as f:
            config = json.load(f)
        host = config['host']
        user = config['user']
        passwd = config['passwd']
        database = config['database']
        stocks = config['stocks'].keys()

        logging.basicConfig(filename='logfile.log', level=logging.INFO, format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %H:%M:%S')

        try:
            self.db = dbapi.connect(host=host, user=user, passwd=passwd, database=database)
            self.init_db(stocks)
        except dbapi.DatabaseError as e:
            logging.error(f'Error: {e}')

    def __del__(self):
        if self.db:
            self.db.close()

    def init_db(self, stocks):
        for stock in stocks:
            db_name = f'{stock}_stocks'

            cursor = self.db.cursor()
            cursor.execute(f'SELECT * FROM information_schema.tables WHERE table_name = "{db_name}"')
            if not cursor.fetchone():
                logging.info(f"Table for {stock} not exists yet, creating...")
                cursor.execute(f'CREATE TABLE {db_name} (Id VARCHAR(255) PRIMARY KEY, Open FLOAT(25), High FLOAT(25), Low FLOAT(25), Close FLOAT(25), Volume FLOAT(25));')

    def save(self, stock):
        db_name = f'{stock}_stocks'
        collector = StockPriceDataCollector()
        stock_data = collector.get_data(stock)

        cursor = self.db.cursor()
        n = 0
        for data in stock_data:
            row = data.get_tuple()

            try:
                sql = f'INSERT INTO {db_name} (Id, Open, High, Low, Close, Volume) VALUES (%s, %s, %s, %s, %s, %s);'
                cursor.execute(sql, row)
            except IntegrityError:
                continue
            n += 1
        self.db.commit()
        logging.info(f'{n} new items saved for {stock}.')

    def export(self, stock):
        db_name = f'{stock}_stocks'
        yield ('Date', 'Open', 'High', 'Low', 'Close', 'Volume')
        cursor = self.db.cursor()
        cursor.execute(f'SELECT * FROM stocks.{db_name} ORDER BY Id ASC')
        for item in cursor.fetchall():
            yield item
