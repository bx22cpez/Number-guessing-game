import random

number=random(1,9)
chances=0

while chances < 5:
    guess=int(input("Enter guess"))
    if guess == number: 
        print("Congratulations you WON!!!!!")
        break
    
    else :
        print("Try again")
        chances - 1




    if not chances < 5:
        print("You lose. The correct number is", number)