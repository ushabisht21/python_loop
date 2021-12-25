num = int(input("Enter a number: "))
i=1
count=0
while i<=num:
    if num%i==0:
        count=count+1
    i=i+1
if count==2:
    print(num,"is a prime number")
else:
    print(num,"not a prime number")


