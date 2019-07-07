import pandas_datareader.data as web
import pandas as pd
import numpy as np
import os
import talib as ta
import matplotlib as plt
from time import sleep


import csv
df=pd.read_csv('/Applications/MT4.app/Contents/Resources/drive_c/Program Files (x86)/MetaTrader - EXNESS/MQL4/Files/XAUUSDmDaTa1.csv')
Data={}
#Dataprice=pd.DataFrame(df,columns=["CLOSE"])
Dataprice = df["CLOSE"].tolist()
s=df["CLOSE"].tolist()
v=df.to_dict()
print(v,"sssss")
#print(Dataprice)
#print(len(Dataprice))

d=[]
Datahigh=df["HIGH"].iloc[89:100].tolist()

#time=df["TIME"].iloc[89:100].tolist()
#print(Datahigh)
#print(time)
#print(df.iloc[0])
'''''
def main():
    while True:
        try:
            if
        except:
            continue
    sleep(1)
def sendorder(type,orderID,takeprofit):
    if type="sell":

    return p
'''


DataATR=df["ATR"]
c=ta.EMA(df["CLOSE"],10)
a=ta.SMA(df["CLOSE"],10)
'''''
for i in range(len(Dataprice)-1,-1,-1):

    print(Dataprice[i],"and ",i)
#reverse list ก่อน นำไปใช้ Dataprice.reverse()
#print(df)

b=ta.RSI(df["CLOSE"],14)

dfRange=df.iloc[0:47]
#for i in Dataprice:
 #   print(i,"sss")

#print(a," and EMA ",c)




Pair="EURUSDm"
df=pd.DataFrame({'': [Pair+','+signal+','+str(SL)+','+str(TP),',,,']})
df=df.to_csv("C:\\Users\\t\\AppData\\Roaming\\MetaQuotes\\Terminal\\61007F75C6EC7CED9A269B292061D7A1\\MQL4\\Files\\LastSignal.csv", header=None, index=None, mode='w', sep=' ',quoting=csv.QUOTE_NONE, quotechar="-",  escapechar="-")
'''
