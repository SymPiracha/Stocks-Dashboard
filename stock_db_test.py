from iexfinance.stocks import get_historical_data
from datetime import datetime

api_key = 'pk_495c80fadacc450e8d8912f83b9d4053'

#stock = Stock('TSLA',token=api_key)

start = datetime(2021, 1, 21)
end = datetime(2021, 1, 29)

df = get_historical_data("TSLA", start, end,token=api_key)

print(df)

