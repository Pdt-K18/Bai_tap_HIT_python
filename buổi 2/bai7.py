def tong(n):
    sum=0
    for i in range(1,n//2+1) :
        if n % i == 0 :
            sum+=i
    return sum
n = int(input("Nhap n = "))
for i in range(1,n+1) :
    k=tong(i)
    if i==tong(k) and i<k : print(i," ",k)
    
    
        

