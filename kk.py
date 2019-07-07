import numpy
import time

#fibonacci

retracements = [23.6,38.2,50.00,61.8,76.4,78.6,85.40]
extensions = [127.2,138.2,150.00,161.8,176.4,261.8,423.6]
high = float(input('Enter High: '))
low = float(input('enter Low: '))
diff = high - low
def uptrend():
    print('\n\t\tUPTREND\t\n')
    print('Retracements\t\tExtensions\n')
    for r, e in zip(retracements, extensions):
        print(r, ' = ', round((high - (diff * r / 100)), 2), '\t', e, ' = ', round((low + (diff * e / 100)), 2), '\n')


def downtrend():
    print('\n\t\tDOWNTREND\t\n')
    print('Retracements\t\tExtensions\n')
    for r, e in zip(retracements, extensions):
        print(r, ' = ', round((low + (diff * r / 100)), 2), '\t', e, ' = ', round((high - (diff * e / 100)), 2), '\n')


#for high
lowlist2=[0.11,0.2,0.12,0.25,0.19,0.25,0.23]
highlist2=[0.19,0.21,0.4,0.2]
lowlist2=list(sorted(lowlist2))
highlist2=list(sorted(highlist2))
lasti=lowlist2[0]
for i in range(1,len(lowlist2)):
    diff=abs(lasti-lowlist2[i])
    percent=diff/lasti*100
    if percent<20:
        print(i,"iiiiii1",lowlist2[i])
    else:

        print(i,"iiiiiiiii2",lowlist2[i])
    lasti=lowlist2[i]


low=min(lowlist2, key=lambda y: tickclose>y and  abs(y - tickclose) )
high=min(highlist2, key=lambda y: tickclose>y and abs(y - tickclose) )
print(low,"low2")
print(high,"high2")

sellorder={}

sellorder.setdefault("takeprofit",[]).append(0.5)
sellorder.setdefault("takeprofit",[]).append(1.0)
sellorder.setdefault("takeprofit",[]).append(1.2)
sellorder.setdefault("number",[]).append(4)
sellorder.setdefault("number",[]).append(6)
sellorder.setdefault("number",[]).append(7)
x=list(sellorder["takeprofit"]).index(1.2)
print(sellorder["number"][x],"number ksaldkas;")

sellorder.setdefault("data",[]).append([1,2,3])
sellorder.setdefault("data",[]).append([2,2,3])
print()


print(sellorder["data"])
#for i in sellorder["takeprofit"]:
a=[1,0]
print(max(a))
print()
a={}
a.setdefault("sad",[]).append(2)
b={}
b.setdefault("sad",[]).append(3)
s={}
s.update(a)
s.update(b)
print(s,"ssss")
order=[["sell",0],["buy",1]]
order.append(["buy",2])
for i in order:
    print(i)
    if i[0]=="buy":
        print("fuck")
G2={}
G2.setdefault("high",[]).append(2)
G2.setdefault("high",[]).append(3)
G2.setdefault("high",[]).append(3)
G2.setdefault("low",[]).append(1)
G2.setdefault("low",[]).append(0)
G2.setdefault("low",[]).append(0)
for i in range(3):
    print(G2["high"][i],"G22222")
