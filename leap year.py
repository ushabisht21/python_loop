year=int(input("enter the number:"))
if year%4==0:
    print("givin year is a leap year")
else:
    print("given year is not a leap year")    





a=int(input("enter the year"))
b=int(input("enter the year"))
while a<=b:
    if a%4==0 and a%100!=0 :
        print(a,"year is leap year")
    else:
        print(a,"is not leap year")
    a=a+1     



num=int (input("enter the number "))
if num >= 0:
    if num ==0:
        print ("zero")
    else:
        print ("positive number")  
else:
    print("negative number")