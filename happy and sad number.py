num=int(input("enter the number"))
a=num
while sum!=1 and sum!=4:
    sum=0
    while a!=0:
        rem=int(a%10) 
        sum=sum+rem*rem 
        a=a//10
    a=sum
if sum==1:
    print(num,"ts a happy number")  
else:
    print(num,"is a sad number")          

