import requests
import pandas as pd
from prettytable import PrettyTable
import json
import pandas as pd

#Create  pretty table object
tableobj=PrettyTable()
keyVal='a36ed32c-781d-4fab-848f-0b0776701e45'
api_endpoint='https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY='+keyVal
# print(api_endpoint)

"""url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# parameters = {
#   'start':'1',
#   'limit':'5000',
#   'convert':'USD'
# }
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'a36ed32c-781d-4fab-848f-0b0776701e45',
}"""

json_data=requests.get(api_endpoint).json()
# print(json_data)
cryptodata=json_data['data']
print(cryptodata)
name=[]
price=[]
oneh_change=[]
oneday_change=[]
sevenday_change=[]
for currency in cryptodata:
    curr_name=currency['name']
    name.append(curr_name)
    curr_price=currency['quote']['USD']['price']
    price.append(curr_price)
    curr_change_1h=currency['quote']['USD']['percent_change_1h']
    oneh_change.append(curr_change_1h)
    curr_change_24h=currency['quote']['USD']['percent_change_24h']
    oneday_change.append(curr_change_24h)
    curr_change_7d=currency['quote']['USD']['percent_change_7d']
    sevenday_change.append(curr_change_7d)
    # print(curr_name,curr_price,curr_change_1h,curr_change_24h,curr_change_7d)

field_names=['Currency Name',"Currency Price","Currency 1h change","Currency 24h change","Currency 7d change"]
# print(field_values)
df=pd.DataFrame(data=zip(name,price,oneh_change,oneday_change,sevenday_change),columns=field_names)
print(df)
csv_data = df.to_csv("cryptodata.csv")