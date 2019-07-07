#from CsvReader import Data
import numpy
import time
from collections import OrderedDict
class CheckRange():
    def __init__(self):
        self.Series=[]
        self.laststd=10
        self.lastseries={}
        self.Price=[]
        self.Series.append([1,0])
        self.Price.append([1.0,0.01])
        self.mean=0
        self.numbar=4


    def ok(self):
        print(self.Series, "Series kuy kuy")
    def Range(self,s,type):
        bar=[]
        z=len(s["Price"])


        if z>=2:
            print(s)


            if type=="uptrend":
                s.setdefault("Bars", []).append(self.Series[-1][-1])
                s.setdefault("Price", []).append(self.Price[-1][-1])
                bar = list(reversed(sorted(s["Bars"])))
                price=list(reversed(sorted(s["Price"])))
                print(bar)
                highprice=price[-1]
                lowprice=price[0]
            else:
                s.setdefault("Bars", []).append(self.Series[-1][-1])
                s.setdefault("Price", []).append(self.Series[-1][-1])
                bar = list(reversed(sorted(s["Bars"])))
                price = list(reversed(sorted(s["Price"])))
                highprice=price[0]
                lowprice=price[-1]

#ผิด มันต้องใช้ max กับ min แทน mean
            if highprice>self.mean+0.33*self.laststd or lowprice<self.mean-0.33*self.laststd or 1/3*len(bar)>self.numbar :
                print("fuckyeah")
                self.Series.append([bar[0],bar[-1]])
                self.Price.append([price[0],price[-1]])
            else:
                print("no")
                n=[]
                p=[]

                for i in bar:
                    n.append(bar[i])
                    p.append(price[i])
                n=n+self.Series[-1]
                print(n,"nnnn")
                    #self.Price=list(reversed(sorted(self.Price)))

                max1=max(n)
                min1=min(n)
                del self.Series[-1]
                print(max1,min1,"kids")
                self.Series.append((max1,min1))

            print(self.Series,"asdsadsad")
            self.numbar = abs(self.Series[-1][0]-self.Series[-1][-1])+1
            print(self.numbar,"numbar")
            k = numpy.std(price)
            self.max=max()
            self.laststd=k

            CheckRange.ok(self)











