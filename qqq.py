import pandas as pd
import time
import numpy
series={}
series.setdefault("hour",[])
series.setdefault("day",[])
r=[1,2,3,4]
Order=[]
order=pd.read_csv('/Applications/MT4.app/Contents/Resources/drive_c/Program Files (x86)/MetaTrader - EXNESS/MQL4/Files/Orders.csv')
dftick=pd.read_csv('/Applications/MT4.app/Contents/Resources/drive_c/Program Files (x86)/MetaTrader - EXNESS/MQL4/Files/BTCUSDmTick.csv')
print(dftick)
symbol=order["Symbol"]
Typeorder=order["Typeorder"]
Takeprofit=order["Takeprofit"]
print(Typeorder)

for i,j,k in zip(Typeorder,symbol,Takeprofit):
    Order.append([i,j,k])

print(Order)
if Order[0][0]=="sell":
    print("sdads")
print(len(Order),"len")
series["day"]=[]
series["day"].extend(r)
print(series)