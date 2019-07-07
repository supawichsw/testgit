from CsvReader import Dataprice
import orderdict

import lol
class ConstructWave():
    def __init__(self):


        ClosePricesarray=CsvReader.i
        highPricesarray=CsvReader.
        lowPricesarray=CsvReader.
        ExtremeHigh=highPricesarray[0]
        ExtremeLow=lowPricesarray[0]
        k="none"

        self.Downtrend={}
        self.Uptrend={}
        newhigh=0
        Lastlow=0
        Lasthigh=0
        newlow=0
        t=lol.CheckRange()


        for i in range(len(ClosePricesarray),0,-1):

             #find extreme low and high from data 300 bars หาจุด max(highPricesarray) min(lowPricesarray)
            if lowPricesarray[i]<ExtremeLow or highPricesarray[i]<ExtremeHigh:
                ExtremeLow=lowPricesarray[i]
                ExtremeHigh=highPricesarray[i]
                newlow=i
                self.Downtrend.setdefault("Bars", []).append(newlow)
                self.Downtrend.setdefault("Price", []).append(lowPricesarray[newlow])
                k="downtrend"
                if Lastlow == newlow:

                    newlow = -1
                    t.Range(self.Downtrend,k)
                    self.Downtrend={}

            elif highPricesarray[i]>ExtremeHigh or lowPricesarray[i]>ExtremeLow:
                ExtremeHigh=highPricesarray[i]
                ExtremeLow=lowPricesarray[i]
                newhigh=i
                self.Uptrend.setdefault("Bars", []).append(newhigh)
                self.Uptrend.setdefault("Price", []).append(highPricesarray[newhigh])
                k="uptrend"
                if Lasthigh==newhigh:
                    newhigh = -1
                    t.Range(self.Uptrend,k)
                    self.Uptrend={}
            else:# highPricesarray[i]>ExtremeHigh and lowPricesarray[i]<ExtremeLow:
                ExtremeHigh = highPricesarray[i]
                ExtremeLow = lowPricesarray[i]
                if k=="uptrend":
                    t.Range(self.Uptrend,k)
                elif k=="downtrend":
                    t.Range(self.Downtrend,k)
                if highPricesarray[i]>0.33*t.laststd+t.mean:
                    #self.uptrend
                    print("fuck")
                elif lowPricesarray[i]<0.33*t.laststd+t.mean:
                    print("kuy")
                else:
                    #find diff price on high and low and use max on diff if max diff is high self.uptrend and no diff "=" if k=up ว่าไป


            else:
                if k=="uptrend":
                    ExtremeHigh = highPricesarray[i]
                    ExtremeLow = lowPricesarray[i]
                    newhigh = i
                    self.Uptrend.setdefault("Bars", []).append(newhigh)
                    self.Uptrend.setdefault("Price", []).append(highPricesarray[newhigh])
                elif k=="downtrend":
                    ExtremeLow = lowPricesarray[i]
                    ExtremeHigh = highPricesarray[i]
                    newlow = i
                    self.Downtrend.setdefault("Bars", []).append(newlow)
                    self.Downtrend.setdefault("Price", []).append(lowPricesarray[newlow])
                else:
                    print("nothing")

                
            Lastlow=newlow
            Lasthigh=newhigh



                #หา mean จาก barrange แล้วใช้ 1.33sd กับ barrange

























        #ถ้า slope มันเปลี่ยน
