#from CsvReader import Dataprice,DataATR
import CsvReader
import orderdict
import Linenotify
import test2
import os
import numpy
class breakout():

    def __init__(self,Pair,Trend,diff,highlist,lowlist,ATR,lasthigh,lastlow,lastopen,lastclose): #ประกาศใช้ทุก 1 ชม
        self.Pair=Pair

        self.Order=[]
        self.lasthigh=lasthigh
        self.lastlow=lastlow
        self.orderID=0
        self.lasttrend=Trend[-1]
        self.lasttrend2=Trend[-2]
        self.meandiff=numpy.mean(diff)
        self.ATR=ATR[-1]
        self.lowlist2=lowlist
        self.highlist2=highlist
        print(self.lowlist2["day"],"dsadsadas")
        self.highlist = list(sorted(highlist["hour"]))
        self.lowlist = list(reversed(sorted(lowlist["hour"])))
        print(lastlow,"and",self.lowlist)
        if lastlow<min(self.lowlist):
            self.lowlist=list(reversed(sorted(lowlist["day"])))
        if lasthigh>max(self.highlist):
            self.highlist=(list(sorted(highlist["day"])))

        self.low = min(self.lowlist, key=lambda y: lastlow < y and abs(y - lastlow))
        self.high= min(self.highlist, key=lambda y: lasthigh > y and abs(y - lasthigh))
        self.diffopenclose=lastclose-lastopen
        self.lastdiff=diff[-1]
        self.HighTP=-1
        self.LowTP=-1
        self.High=0
        self.Low=0
        self.ATR2=ATR[-2]
        self.openbuy=0
        self.opensell=0
        self.Order=[]





    def ATRtick(self,sdlow,sdhigh,tickclose,tickopen,Order,ticklow,tickhigh,tickATR,sdlowday,sdhighday):#ใช้กับ tick data เป็น tick trend tick close
        self.Order=Order

        sellmodify=False
        buymodify=False
        s1=0
        s2=0
        sellorder=False
        buyorder=False
        SELLoldTP=[]
        BUYoldTP=[]
        tickdiff=abs(tickhigh-ticklow)
        if self.lasthigh>tickhigh:
            Lasthigh=self.lasthigh
        elif self.lasthigh<tickhigh:
            Lasthigh=tickhigh


        if self.lasttrend=="up" and tickclose<sdlowday and tickATR>self.ATR and abs(tickclose-tickopen)*2>abs(self.diffopenclose):
            print("sell is opened kuy rai")
            print(self.lasttrend,"kuy rai ar")
            sellorder=True
            Typeorder=1



                #send

        elif self.lasttrend=="down" and tickclose>sdhighday and tickATR>self.ATR and abs(tickclose-tickopen)*2>abs(self.diffopenclose):
            print("buy is opened")
            buyorder=True



        if self.lasttrend=="up":

            Added =(tickhigh-self.low)*18/100 #(f if f > 0.8 else 0.8)
            pricebreak = self.high+Added
            if tickclose >= pricebreak:#เป็นการเบรก แนวต้าน
                if tickATR > self.ATR and abs(tickclose-tickopen)*1.50>abs(self.diffopenclose):
                    buyorder = True



                #send csv file an open buy order to mt4

        elif self.lasttrend=="down":
            Added= (self.high-ticklow)*18/100 #(f if f>0.8 else 0.8)
            pricebreak = self.low-Added
            if tickclose<=pricebreak :
                if tickATR > self.ATR and abs(tickclose - tickopen) * 1.50 > abs(self.diffopenclose):
                    sellorder = True

                    print("open sell")


        if len(Order)>0:
            for i in Order:
                if i[0] == "sell" :#i[4]=ticket
                    s1=s1+1
                    if tickclose<self.LowTP and abs(tickclose-tickopen)>abs(self.diffopenclose):#i[3] = takeprofit
                        sellmodify=True


                    if tickclose>sdhigh or (tickdiff>self.lastdiff and tickclose<tickopen and tickclose>=ticklow+(0.3*(tickopen-ticklow)) )or (self.lastdiff<0.3*self.meandiff and self.ATR2>self.ATR) : #or (self.lasttrend!="down")  :#trailing profit มาจาก if tickclose<tickopen and tickclose>=ticklow+0.3(tickopen-ticklow)
                        if tickclose>sdhigh:
                            print("1 sell")
                        if tickclose<tickopen and tickclose>=ticklow+(0.3*(tickopen-ticklow)) :
                            print("2 sell")
                        if self.lastdiff<0.3*self.meandiff and self.ATR2>self.ATR:
                            print("3 sell")
                        if self.lasttrend!=self.lasttrend2:
                            print("4 sell",self.lasttrend,self.lasttrend2)
                        msg="CLOSE: sell order "+self.Pair
                        Linenotify.Linenotify(msg)


                if i[0] == "buy":
                    s2=s2+1
                    if tickclose > self.HighTP and abs(tickclose - tickopen) > abs(self.diffopenclose):  # i[3] = takeprofit
                        buymodify=True



                    if  tickclose<sdlow or (tickdiff>self.lastdiff and tickclose>tickopen and tickclose<=tickhigh-(0.3*(tickhigh-tickopen))) or (self.lastdiff<0.3*self.meandiff and self.ATR2>self.ATR) or self.lastesthigh:# or #(self.lasttrend!="up")  :
                        if tickclose<sdlow:
                            print("1 buy")
                        if tickclose>tickopen and tickclose<=tickhigh-(0.3*(tickhigh-tickopen)):
                            print("2 buy",tickclose,tickopen,tickhigh,tickhigh-(0.3*(tickhigh-tickopen)))
                        if self.lastdiff<0.3*self.meandiff and self.ATR2>self.ATR:
                            print("3 buy")
                        if self.lasttrend!=self.lasttrend2:
                            print("4 buy",self.lasttrend,self.lasttrend2)
                        msg = "CLOSE: Buy order " + self.Pair
                        Linenotify.Linenotify(msg)
                        os.remove('/Applications/MT4.app/Contents/Resources/drive_c/Program Files (x86)/MetaTrader - EXNESS/MQL4/Files/Orders.csv')



        print(sellorder,"order and ",buyorder,"order")

        if sellorder or sellmodify:

            low,Type = test2.Takeprofit("down", self.lowlist2["hour"], self.highlist2["hour"], self.lowlist2["day"],
                                   self.highlist2["day"], tickclose, self.lowlist2["day"][-1],
                                   self.highlist2["day"][-1])
            self.LowTP=low
            if s1<2 and sellorder :
                self.LowTP
                msg="Open sell order "+self.Pair+"New TP: "+low
                Linenotify.Linenotify(msg)

            if sellmodify:
                msg="Modify SELL order "+self.Pair+"New TP: "+low+" Close another sell"
                Linenotify.Linenotify(msg)



        elif buyorder or buymodify :
            print(self.lowlist2["day"],"day")
            self.High,Type = test2.Takeprofit("up", self.lowlist2["hour"], self.highlist2["hour"], self.lowlist2["day"],
                                   self.highlist2["day"], tickclose, self.lowlist2["day"][-1],
                                   self.highlist2["day"][-1])

            if s2<2 and buyorder and self.HighTP!=self.High:
                self.HighTP = self.High
                msg = "Open buy order " + self.Pair + "New TP: " + str(self.High)
                Linenotify.Linenotify(msg)

            if buymodify  and self.HighTP!=self.High:
                self.HighTP = self.High
                if s2==2:
                    msg = "Modify BUY order " + self.Pair + "New TP: " + str(self.High)+" Close another buy"
                    Linenotify.Linenotify(msg)
                elif s2==1:
                    msg= "Modify BUY order " + self.Pair + "New TP: " + str(self.High)
                    Linenotify.Linenotify(msg)








            # sendorder


if __name__ == '__main__':
    G2={}
    G2.setdefault("sdlow",[]).append(3)
    G2.setdefault("sdlow", []).append(3)
    G2.setdefault("sdlow", []).append(4)
    G2.setdefault("sdhigh", []).append(5)
    G2.setdefault("sdhigh", []).append(6)
    G2.setdefault("sdhigh", []).append(7)
    G2.setdefault("tickclose",[]).append(5.8)
    G2.setdefault("tickclose", []).append(5.8)
    G2.setdefault("tickopen",[]).append(2)
    G2.setdefault("tickopen", []).append(2)
    G2.setdefault("ticklow",[]).append(2)
    G2.setdefault("ticklow", []).append(2)
    G2.setdefault("tickhigh",[]).append(5.8)
    G2.setdefault("tickhigh", []).append(5.8)
    order=[]
    order2=[]
    #order=[open,pair,tp,ticket]
    order.append(["buy","EURUSDm",5,1020,1])
    order2.append(["buy", "EURUSDm", 5, 1020])








    highlist2=[3,5,6]
    lowlist2=(2,4,5)
    ATR=1.00
    c=breakout("Eurusd","up",0.6,highlist2,lowlist2,ATR,4,3,order)

    #c.ATRtick(G2["sdlow"][0],G2["sdhigh"][0],G2["tickclose"][0],G2["tickopen"][0],order,G2["ticklow"][0],G2["tickhigh"][0],1.5)

    for i in range(2):
        print(i,"i")
        c.ATRtick(G2["sdlow"][i], G2["sdhigh"][i], G2["tickclose"][i], G2["tickopen"][i], order, G2["ticklow"][i],G2["tickhigh"][i], 1.5)

'''''
    for i in range(3):
        c.ATRtick()
        G2["high"][i]


'''


        #ส่งคำสั่งซื้อ  หรือ ขาย ถ้า sd ทะลุและ Tick ATR >  ATR[-1] ทะลุ  และ  close มากกว่า close เก่า 1.30 เท่า


#if a=="break":

   #ดูที่ค่า sd เป็นหลัก  // ถ้า sd ไม่ทะลุ เช็คที่ close ถ้า close ใหม่ น้อยกว่า 30 % ของ close เก่า ขาย

#else:
 #   if diffprice ลดลง





















                    #ทะลุแล้ว แต่ 1)diffprice ลดลง ATR เพิ่ม 2) diffprice เพิ่ม ATR เพิ่ม 3)diffprice ลดลง ATR ลดลง 4)diffprice เพิ่ม ATR ลดลง


'''''
            elif Trend=="down":
                b = min(lowlist, key=lambda y: abs(y - close))
                if k<=1.10*b:
                    print("already break")

                else:

                    print("not yet")
            self.last_ATR = new_ATR
            self.lastdiffprice = diffprice


            if new_i>self.last_i and diffprice=="positive": #diffprice positive คือ ระยะprice มีช่วงกว้างขึ้น ไม่ว่าจะเป็นขึ้น หรือ ลง เช่น เทรนขาขึ้นhighใหม่ต้องมากกว่า close ใหม่ อย่างต่ำ กี่เปอร์เซนต์
                print("yes")
            elif new_i>self.last_i and diffprice=="negative": #คือ ระยะprice มีช่วงลดลง
                print("no")
            


#diffClose=previousClose-currentClose

if __name__ == '__main__':
    s=0
    #ATR(ATR,Dataprice)
    ATR={}
    ATR.setdefault("1hour",[]).append("kuy")
    ATR.setdefault("1hour", []).append("kut")
    for i in ATR["1hour"]:
        print(i,"for")

    print(ATR["1hour"][1])
    #lol=ATR*diffClose

'''