import json
import pymysql as dbapi

from pymysql.err import IntegrityError
from stock_price_data_collector import StockPriceDataCollector
# SQL setting
# - GRANT ALL PRIVILEGES on *.* to 'root'@'localhost' IDENTIFIED BY '<password>';
# - FLUSH PRIVILEGES;

class StockPriceSaver:
    def __init__(self, stock):
        self.stock = stock
        self.db_name = f'{self.stock}_stocks'

        with open('config.json') as f:
            config = json.load(f)
        host = config['host']
        user = config['user']
        passwd = config['passwd']
        database = config['database']

        try:
            self.db = dbapi.connect(host=host, user=user, passwd=passwd, database=database)
            cursor = self.db.cursor()
            cursor.execute(f'SELECT * FROM information_schema.tables WHERE table_name = "{self.db_name}"')
            if not cursor.fetchone():
                print(f"Table for {stock} not exists yet, creating...")
                cursor.execute(f'CREATE TABLE {self.db_name} (Id VARCHAR(255) PRIMARY KEY, Open FLOAT(25), High FLOAT(25), Low FLOAT(25), Close FLOAT(25), Volume FLOAT(25));')
        except dbapi.DatabaseError as e:
            print(f'Error: {e}')

    def __del__(self):
        if self.db:
            self.db.close()

    def save(self):
        collector = StockPriceDataCollector()
        stock_data = collector.get_data(self.stock)

        cursor = self.db.cursor()
        n = 0
        for data in stock_data:
            row = data.get_tuple()

            try:
                sql = f'INSERT INTO {self.db_name} (Id, Open, High, Low, Close, Volume) VALUES (%s, %s, %s, %s, %s, %s);'
                cursor.execute(sql, row)
            except IntegrityError as e:
                continue
            n += 1

        self.db.commit()
        print(f'{n} new items saved.')
