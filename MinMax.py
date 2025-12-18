a,b,c=map(int,input().split())
if (a<=b and a<=c):
    min=a
elif (b<=a and b<=c):
    min=b
else:
    min=c
if (a>=b and a>=c):
    max=a
elif (b>=a and b>=c):
    max=b
else:
    max=c
print(min,max)