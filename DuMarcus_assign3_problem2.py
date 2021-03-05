"""
Marcus Du
2/25/2021
Section 006
Problem #2: Guess the Number Game
"""
from random import *
tries=0
ans=randint(1,10)
print("I'm thinking of a number between 1 and 10!")
while tries<3:
    guess=int(input("What's your guess?"))
    if guess==ans:
        print("You got it!")
        print("The secret number was",ans)
        tries=tries+1
        print("It took you",tries,"tries to guess the number")
        break
    elif guess<ans and tries<2:
        print("Too low, try again.")
        tries=tries+1
    elif guess>ans and tries<2:
        print("Too high, try again.")
        tries=tries+1

    elif tries>=2 and guess!=ans:
        print("The secret number was",ans)
        print("You didn't guess the number.")
        break
    
