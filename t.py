
if False:
    from datetime import datetime, timezone
    import pytz
    utc_dt=datetime.now(timezone.utc)
    JST=pytz.timezone('EasternTime')
    output = "{}".format(utc_dt.astimezone(JST).isoformat())
    time = output.split("T")[-1]
    timeList = time.split(":")
    timeOut = timeList[0]+":"+timeList[1]
    print(timeOut + " " + JST.zone)


if False:
    import yaml
    config = yaml.safe_load(open("takushi/static/takushi/keys/keys.yml"))
    print(config['weatherApi'])

    import requests
    api_url = "http://api.weatherapi.com/v1/current.json"
    api_url += "?key="+config['weatherApi']
    api_url += "&q=Osaka&aqi=yes"
    print("api_url = "+api_url)

    response = requests.get(api_url)
    responseJSON = response.json()
    print("name = "+ responseJSON['location']['name'])
    print("localtime = "+responseJSON['location']['localtime'])
    print("temp_c = "+str(responseJSON['current']['temp_c']))
    print("temp_f = "+str(responseJSON['current']['temp_f']))
    print("humidity = "+str(responseJSON['current']['humidity']))


import yfinance as yf
import time
import pandas as pd
from datetime import date
import numpy as np

start_time = time.time()

def reqFinData(symbolList):
    # download data
    data = yf.download(tickers=symbolList, group_by='Ticker', period="1y", interval="3mo")
    print(data)

    dataList = []
    for i in symbolList:
        # use Adjusted Close as most important data
        adjClose = data[i]['Adj Close']

        # get most recent data
        idx_r = adjClose.last_valid_index()
        close_r = adjClose[idx_r]
        open_r = data[i]['Open'][idx_r] #get 'Open' with most recent index
        date_r = idx_r.isoformat()

        # get most historic data
        idx_h = adjClose.first_valid_index()
        date_h = idx_h.isoformat()
        close_h = adjClose[idx_h]

        data_t = {'date_h':date_h,'close_h':close_h,'date_r':date_r,'open_r':open_r,'close_r':close_r}

        dataList.append({'symbol':i,'data':data_t})
    return dataList

symbolList = ['^GSPC','^DJI','^N225','BTC-USD','JPY=X','EURUSD=X','GC=F','CL=F']
print(reqFinData(symbolList))
# print(data['BTC-USD']['Open'].head(1).index.date[0].isoformat())

# print(msft.info['currentPrice'])
print("--- %s seconds ---" % (time.time() - start_time))


# msft.info

# hist = msft.history(period="max")
# print(hist)
#
# print(msft.institutional_holders)
