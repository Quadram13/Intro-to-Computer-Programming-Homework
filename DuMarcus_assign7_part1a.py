"""
Marcus Du
4/2/2021
Section 006
Part 1a
"""
allcon=False
length= False
FLchar=False
UPchar=False
LOWchar=False
NUMchar=False

while allcon==False:
    username=""
    num_cap=0
    num_low=0
    num_digits=0
    username=str(input("Enter a username: "))
    print("* Length of username: ",len(username))
    if len(username)<8 or len(username)>15:
        length=False
    else:
        length=True
    print("* All characters are alpha-numeric: ",username.isalnum())
    if username[0].isalpha()==True and username[-1].isalpha()==True:
        FLchar=True
    else:
        FLchar=False
    print("* First & last characters are not digits: ",FLchar)    
    for i in range (65,91):
        num_cap+=username.count(chr(i))
    if num_cap<1:
        UPchar=False
    else:
        UPchar=True
    print("* # of uppercase characters in the username: ",num_cap)
    for i in range (97,123):
        num_low+=username.count(chr(i))
    if num_low<1:
        LOWchar=False
    else:
        LOWchar=True
    print("* # of lowercase characters in the username: ",num_low)
    for i in range (48,58):
        num_digits+=username.count(chr(i))
    if num_digits<1:
        NUMchar=False
    else:
        NUMchar=True
    print("* # of digits in the username: ",num_digits)
    if length==True and FLchar==True and username.isalnum()==True and UPchar==True and LOWchar==True and NUMchar==True:
        allcon==True
        print("Username is valid!")
        break
    else:
        print("Username is invalid, please try again")
        print()
        


        


