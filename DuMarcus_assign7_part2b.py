"""
Marcus Du
4/2/2021
Section 006
Part 2b
"""
from DuMarcus_assign7_part2a import *

wtd=""
while wtd!="q":
    wtd=input("(e)ncode, (d)ecode or (q)uit: ")
    if wtd=="e":
        num=int(input("Enter a number between 1 and 5: "))
        word=input("Enter a phrase to encode: ")
        print("Your encoded word is: ",shift_characters(add_letters(word,num),num))
    
    elif wtd=="d":
        num=input("Enter a number between 1 and 5: ")
        word=input("Enter a phrase to encode: ")
        print("Your decoded word is: ",remove_letters(shift_characters(word,-num),num))

