import random

rand = random.randint(1,9)
print(rand)

chances = 0
while chances<5:
    Number = int (input("Guess the number(Between 1 and 9)"))
    if Number==rand:
        print("Congratulations! you won the game")
        break
    elif Number<rand:
        print("Guess a higher number")
    else :
        print("Guess a lower number")

    chances = chances+1

if not chances<5:
    print("You loose the game")