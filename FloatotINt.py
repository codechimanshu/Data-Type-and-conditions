# a=input()
# x=a.split(".")
# if x[1]=='000':
#     print(int(x[0]))
# else:
#     print(x[1]," ",'.',float(0,x[1]))
n=float(input())
m=int(n)
if(n==m):
    print("int",m)
else:
    d=n-m
    print("float",m,f"{d:.3f}")