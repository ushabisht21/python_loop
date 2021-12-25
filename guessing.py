target_number=5
i=1
while i<=10:
    guess_num=int(input("enter the number"))
    if guess_num==target_number:
        print("you win game")
        break
    if i==5:
        print("you loose game")
        break
    else:         
        print("try again")
    i=i+1

        