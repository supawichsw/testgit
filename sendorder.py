import csv
import pandas as pd
import os
#Order ที่ send กลับมาจาก mt4 จะเป็น csv file และ จะถูกเก็บในรูป dict
def sendorderCSV(Typeorder,Pair,Takeprofit,Filename,Ticket=0):
    df = pd.DataFrame({'': [Typeorder + ',' + Pair + ',' + str(Takeprofit) + ',' + str(Ticket)]})
    df.to_csv(Filename, header=None, index=None, sep=' ')
Filename = "/Applications/MT4.app/Contents/Resources/drive_c/Program Files (x86)/MetaTrader - EXNESS/MQL4/Files/LastSignal.csv"

sendorderCSV("Buy","XAUUSDm",1300,Filename)

print(os.path.exists(Filename))