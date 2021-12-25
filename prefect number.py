num=int(input("enter the number:-"))
sum=0
i=1
while i<num :
    if num%i==0:
        sum=sum+i
    i=i+1
if num ==sum :
    print(num,"is a prefect number") 
else:
    print(num,"is not a prefect number")       