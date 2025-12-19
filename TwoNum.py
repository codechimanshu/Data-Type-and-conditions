import math
a,b=input().split()
a=int(a)
b=int(b)
print("floor",a,"/",b,"=",math.floor(a/b))
print("ceil",a,"/",b,"=",math.ceil(a/b))
print("round",a,"/",b,"=",math.floor((a/b)+0.5)+0.53)