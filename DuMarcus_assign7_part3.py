"""
Marcus Du
4/2/2021
Section 006
Part 3
"""

index=0

def string_length(string):
    count=0
    for i in string:
      count=count+1
    return(int(count))

def string_isalpha(string):
    alpha=False
    count_A=0
    
    
    for i in string:
        if 65<=ord(string[index])<=90 or 97<=ord(string[index])<=122:
            count_A+=1
        index+=1
    if count_A==string_length(string):
        alpha=True
    else:
        alpha=False
    print(alpha)

def string_isupper(string):
    count_U=0
    upper=False
    for i in string:
        if 97<=ord(string[index])<=122:
            count_U+=1
            index+=1
        else:
            index+=1
    if count_U==string_length(string):
        upper=True
    else:
        upper=False
    print(upper)
string_isupper("hello")