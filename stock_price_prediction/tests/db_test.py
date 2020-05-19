import json

from stock_price_saver import StockPriceSaver

with open('../config.json') as f:
    config = json.load(f)

saver = StockPriceSaver()

for stock in config['stocks'].keys():
    i = 0
    for line in saver.export(stock):
        i += 1
    print(f'{i} item is stored for {stock}')
