n = int(input("nhap n : "))
S=1
for i in range(2,(2*n)+2) : 
    if i % 2 == 0 : S+=(-1)*i
    else : S+=i
print(S)
#b)
T=0
for i in range(2,n+1) : T+=1/i
print(T)
#c)
a,b,c=map(int,input("Nhap 3 he so cua phuong trinh"))
denta = b*b-4*a*c
if denta > 0 : print("Phương trình có 2 nghiệm phân biệt")
elif denta=0 : print("Phương trình có nghiệm kép")
else : print("Phương trình vô nghiệm")