from test import breakout
import datetime
import time
import os
from orderdict import checker
import pandas as pd





def sendorder(Pair):
    highlist = {}
    lowlist = {}
    highlist.setdefault("hour",[])
    highlist.setdefault("day",[])
    lowlist.setdefault("hour",[])
    lowlist.setdefault("day",[])
    Order=[]

    oldtime=-1
    oldday=-1
    while True:


        if os.path.exists('/Applications/MT4.app/Contents/Resources/drive_c/Program Files (x86)/MetaTrader - EXNESS/MQL4/Files/XAUUSDmDataDay.csv'):

            dfday = pd.read_csv('/Applications/MT4.app/Contents/Resources/drive_c/Program Files (x86)/MetaTrader - EXNESS/MQL4/Files/XAUUSDmDataDay.csv')
            highday = dfday["HIGH"].tolist()
            lowday = dfday["LOW"].tolist()


            d=checker(highday,lowday)
            d.check()
            highlist["day"]=[]
            lowlist["day"]=[]
            highlist["day"].extend(d.highseries)
            lowlist["day"].extend(d.lowseries)
            print(d.lowseries)



            #os.remove('/Applications/MT4.app/Contents/Resources/drive_c/Program Files (x86)/MetaTrader - EXNESS/MQL4/Files/BTCUSDmDataDay.csv')
        if os.path.exists('/Applications/MT4.app/Contents/Resources/drive_c/Program Files (x86)/MetaTrader - EXNESS/MQL4/Files/XAUUSDmDataHour.csv'):
            dfhour = pd.read_csv('/Applications/MT4.app/Contents/Resources/drive_c/Program Files (x86)/MetaTrader - EXNESS/MQL4/Files/XAUUSDmDataHour.csv')
            highhour=dfhour["HIGH"].tolist()
            lowhour=dfhour["LOW"].tolist()
            openlist = dfhour["OPEN"].tolist()
            closelist = dfhour["CLOSE"].tolist()
            ATR=dfhour["ATR"].tolist()


            c=checker(highhour,lowhour)
            c.check()

            highlist["hour"]=[]
            lowlist["hour"]=[]
            highlist["hour"].extend(c.highseries)
            lowlist["hour"].extend(c.lowseries)




           # for i,j in zip(openlist,closelist):
            #    diffopenclose.append(i-j)



            breakout1=breakout(Pair,c.Trend,c.difflist,highlist,lowlist,ATR,highhour[-1],lowhour[-1],openlist[-1],closelist[-1])
            #os.remove('/Applications/MT4.app/Contents/Resources/drive_c/Program Files (x86)/MetaTrader - EXNESS/MQL4/Files/BTCUSDmDataHour.csv')


        if os.path.exists('/Applications/MT4.app/Contents/Resources/drive_c/Program Files (x86)/MetaTrader - EXNESS/MQL4/Files/Orders.csv')==True:
            orders=pd.read_csv('/Applications/MT4.app/Contents/Resources/drive_c/Program Files (x86)/MetaTrader - EXNESS/MQL4/Files/Orders.csv')
            symbol = orders["Symbol"]
            Typeorder = orders["Typeorder"]
            Takeprofit = orders["Takeprofit"]

            for i, j, k in zip(Typeorder, symbol, Takeprofit):
                if j=="XAUUSDm":
                    Order.append([i, j, k])


            print(Order,"Total Order")

        dftick=pd.read_csv('/Applications/MT4.app/Contents/Resources/drive_c/Program Files (x86)/MetaTrader - EXNESS/MQL4/Files/XAUUSDmTick.csv')

        tickhigh = dftick["High"].tolist()
        ticklow = dftick["Low"].tolist()
        tickopen = dftick["Open"].tolist()
        tickclose = dftick["Close"].tolist()
        tickATR = dftick["ATR"].tolist()



        sdlowday,sdhighday,trendday=d.tickcheck()
        sdlow, sdhigh,trend = c.tickcheck()

        breakout1.ATRtick(sdlow,sdhigh,tickclose[0],tickopen[0],Order,ticklow[0],tickhigh[0],tickATR[0])
        print(sdlow,"sdlowww")
        print(c.lowseries)
        print(c.highseries)
        print(c.meanlist)

        time.sleep(1)

sendorder("BTCUSDm")

