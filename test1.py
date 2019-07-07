import time
import numpy
import datetime
import pandas as pd
import sys
import csv
s=time.time()
Pair="EURUSDm"
signal="Buy"
SL=0
TP=1

SL2=2
TP2=2

SL3=2
TP3=2

SL4=3
TP4=9
Filename="/Applications/MT4.app/Contents/Resources/drive_c/Program Files (x86)/MetaTrader - EXNESS/MQL4/Files/LastSignal.csv"
df = pd.DataFrame({'': [Pair+','+signal+','+str(SL)+','+str(TP)]})
df2 = pd.DataFrame({'': [Pair+','+signal+','+str(SL2)+','+str(TP2)]})
df4=pd.DataFrame({'': [Pair+','+signal+','+str(SL3)+','+str(TP3)]})
df5=pd.DataFrame({'': [Pair+','+signal+','+str(SL3)+','+str(TP3)]})
df6=pd.DataFrame({'': [Pair+','+signal+','+str(SL4)+','+str(TP4)]})
df=df.to_csv(Filename, header=None, index=None,sep=' ')
with open(Filename,'a') as f:
     df2.to_csv(f, header=None,index=None,sep=' ')
     df4.to_csv(f,header=None,index=None,sep=' ')
     df5.to_csv(f, header=None, index=None, sep=' ')
     df6.to_csv(f, header=None, index=None, sep=' ')
df3 = pd.read_csv(Filename,names=['symbol','signal','sl','tp'])
listdf3=df3['symbol'].tolist()
listdf4=df3['signal'].tolist()
listdf5=df3.to_dict()
print(listdf3)
print(listdf4)
print(listdf5)
l = time.time()
print(l)
print(l - s, "diff time")