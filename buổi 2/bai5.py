from math import *
n = int(input("Nhap n :"))
for i in range(1,n+1) :
    s=0
    K=i
    while K>0 :
        s+=pow((K%10),3)
        K=K//10
    if i==s : print(i)

    