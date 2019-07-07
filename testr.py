import lol
import orderdict
s={}
x=0
i=0
'''''
s.setdefault("Bars",[]).append(2)
s.setdefault("Price",[]).append(1.130)
s.setdefault("Bars",[]).append(1)
s.setdefault("Price",[]).append(1.115)
s.setdefault("Bars",[]).append(0)
s.setdefault("Price",[]).append(1.125)
z=[]
'''
t=lol.CheckRange()
for i in range(3):
    print(i,"ivalue")
    if i==0:
        s.setdefault("Bars", []).append(-1)
        s.setdefault("Price", []).append(1.130)
    if i==1:
        s.setdefault("Bars", []).append(-2)
        s.setdefault("Price", []).append(1.115)
    if i==2:
        s.setdefault("Bars", []).append(-3)
        s.setdefault("Price", []).append(1.125)

t.Range(s,"uptrend")


''''
while(x<2):
    lol.CheckRange(s)
    i=i-1
    x=x+1
    print(i)
    print(s["Bars"][i],"and",s["Price"][i])
'''