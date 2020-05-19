import json
import yfinance as yf

data = yf.download(tickers="AAPL", period='1d', interval="1m")

print(data)
print(data.columns.values)
alma = data.to_dict(orient='index')
for i in alma:
    print(str(i))
with open('yfinance.json', 'w') as f:
    json.dump(data.to_dict(), f)
