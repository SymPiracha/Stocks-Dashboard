from iexfinance.stocks import get_historical_data
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt

api_key = 'pk_495c80fadacc450e8d8912f83b9d4053' #got the token from the iex finance account.

today = datetime.now().strftime('%Y-%m-%d')  #stored the date when the function is called.

temp = (datetime.now() - timedelta(12)).strftime('%Y-%m-%d') #stores the last 12 days of change.

df = get_historical_data("TSLA", temp, today,token=api_key) #using the api to access the data for a particular stock e.g TSLA

df = df .iloc[3:] # removed the first 3 rows because we are dealing with 5 previous days. (Used 6 to calculate the %change for the 5th day)

df1 = df[['label','close','volume']]

df1.columns = ['date','close','volume']

price_change = []
volume_change = []

#running the forloop to add new columns after computation of these columns namely : %volume_change and %price_change.

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

print(plt.plot(df1['date'],df1['%price_change'],df1['%volume_change']))

#print(df1)
