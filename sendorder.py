import csv
import pandas as pd
#Order ที่ send กลับมาจาก mt4 จะเป็น csv file และ จะถูกเก็บในรูป dict
def sendorderCSV(Typeorder,Pair,Takeprofit,Filename,Ticket=0):
    df = pd.DataFrame({'': [Typeorder + ',' + Pair + ',' + str(Takeprofit) + ',' + str(Ticket)]})
    df.to_csv(Filename, header=None, index=None, sep=' ')
