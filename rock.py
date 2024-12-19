import random
number = random.randint(1,3)
guess= str(input("Make your choice between: rock paper scissor : "))
if(number == 1):
 name="rock"
elif(number == 2):
 name="scissor"
else:
 name="paper"
if(name==guess):
    print("Computer's choice: ",name)
    print("Draw !")
elif(name!=guess):
    print("Computer's choice: ",name)
    if((name=="rock" and guess=="scissor") or (name=="scissor" and guess=="paper") or (name=="paper" and guess=="rock")):
        print("You Loose!")
    else:
        print("You Win!")