n=int(input("Nhap n : "))
S=0
T=1
dem=2
print(S,T,end=" ")
for i in range(0,n+1) : 
    S+=T
    dem+=1
    print(S,end=" ")
    if dem==n : break
    T+=S
    dem+=1
    print(T,end=" ")
    if dem==n : break
        

