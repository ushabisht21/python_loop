a=int(input("enter the number"))
b=a
sum=0
while a>0:
    sum=sum+(a%10)*(a%10)*(a%10)
    a=a//10
if b==sum:
    print("number is armstrong")
else:
    print("number is not armstrong")   

     