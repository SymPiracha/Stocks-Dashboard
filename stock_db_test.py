from iexfinance.stocks import get_historical_data
from datetime import datetime
from datetime import timedelta

api_key = 'pk_495c80fadacc450e8d8912f83b9d4053'

today = datetime.now().strftime('%Y-%m-%d')

#print(today)

yesterday = (datetime.now() - timedelta(12)).strftime('%Y-%m-%d')

df = get_historical_data("TSLA", yesterday, today,token=api_key)

df = df .iloc[3:]

df1 = df[['label','close','volume']]

df1.columns = ['date','close','volume']

price_change = []
volume_change = []

for i in range(5):
    old_price = int(df1.iat[i,1])
    new_price = int(df1.iat[i+1,1])
    old_volume = int(df1.iat[i,2])
    new_volume = int(df1.iat[i+1,2])
    volume_change.append((new_volume-old_volume)/(old_volume)*100)
    price_change.append((new_price-old_price)/(old_price) * 100)
    
df1 = df1.iloc[1:]
df1['%volume_change'] = volume_change
df1['%price_change'] = price_change

print(df1)
