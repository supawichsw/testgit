tick=[0,2,4,6]
z=3

print(tick)
#high2= min(highpricearray,key=lambda y:tickclose>y and y-tickclose >3)
try:
    #For high
    h = min(i for i in tick if i > z and i-z>2 )
    print(h)
except:
    pass
#For low
try:
    y=max(j for j in tick if j <z and z-j >0)
    print(y,"y")
except:
    pass



