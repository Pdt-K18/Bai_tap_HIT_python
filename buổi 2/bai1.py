
a = int(input("nhap so nguyen duong: "))
s=0
while a>0 :
    s+=a%10
    a=a//10
print(s)
n=int(input("Nhap so nguyen dương n: "))
for i in range(1,n+1):
    if n % i == 0: print(i)
x,y,z= map(int,input("nhap 3 canh cua tam giac :").split())
if x+y<z or x+z<y or y+z<x : print("khong phai la tam giac")
elif x==y and y==z : print("day la tam giac deu")
elif x==y or y==z : print("day la tam giac can")
elif x*x+y*y==z*z or x*x+z*z==y*y or y*y+z*z==x*x : print("day la tam giac vuong")
elif x*x+y*y<z*z or x*x+z*z<y*y or y*y+z*z<x*x : print("day la tam giac tu")
else : print("day la tam giac nhon")
