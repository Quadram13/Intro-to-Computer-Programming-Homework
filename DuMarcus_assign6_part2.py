"""
Marcus Du
2/25/2021
Section 006
Part 2
"""
import digitalclock
from random import randint 

numproblems=int(input("How many problems would you like to attempt? "))
while numproblems<=0:
    print("Invalid number, try again")
    numproblems=int(input("How many problems would you like to attempt? "))

width = int(input("How wide do you want your digits to be? 5-10: "))
while width<5 or width>10:
    print("Invalid width, try again")
    width = int(input("How wide do you want your digits to be? 5-10: "))

char=input("What character would you like to use? ")
while len(char)>1 or len(char)<1:
    print("String too long, try again")
    char=str(input("What character would you like to use? "))

print("Here we go!")

numcorrect=0
for i in range(0,numproblems):
    print("What is.....")
    num1=randint(1,9)
    num2=randint(1,9)
    p_or_m=randint(1,2)
    if p_or_m==1:
        operator="+"
    else:
        operator="-"
    digitalclock.print_number(num1,width,char)
    print()
    if operator=="+":
        print(digitalclock.plus(width,char))
    elif operator=="-":
        print(digitalclock.minus(width,char))
    digitalclock.print_number(num2,width,char)
    print()
    ans=int(input("= "))
    print()
    if digitalclock.check_answer(num1,num2,ans,operator)==True:
        print("Correct!")
        numcorrect+=1
    elif digitalclock.check_answer(num1,num2,ans,operator)==False:
        print("Sorry, that's not correct.")
print("You got",numcorrect,"out of",numproblems,"correct!")






        