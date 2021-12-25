n=int(input("enter the number:"))
a=n
sum=0
while a>0:
    r =a%10
    sum=sum+r
    a=a//10
if n%sum==0 :
    print(n,"hurshad number")
else :
    print(n,"not hurshad number")    