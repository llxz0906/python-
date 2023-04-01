import math
r=input("输入圆的半径：")
r=float(r)
c=2*math.pi*r
s=math.pi*math.pow(r,2)
print("圆的周长：",round(c,2))
print("圆的面积：",round(s,2))
