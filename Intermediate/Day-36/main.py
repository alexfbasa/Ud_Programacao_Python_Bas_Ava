from alpha_vantage.timeseries import TimeSeries

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

API_KEY = "TQ0UX34ZXE6KZ6WV"

ts = TimeSeries(key=API_KEY)
data, meta_data = ts.get_daily(symbol=STOCK_NAME)

latest_price = data['4.close'][0]
print(latest_price)
