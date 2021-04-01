"""
Marcus Du
3/25/2021
Section 006
Challenge 4
"""


# next, write a new function called 'simple_sort_version2' that accepts three values.  you can assume
# that your three values will always be the same data type (all ints, all floats or all strings).
# sort these values in ascending order and return them. 
# you may use any function that you've written so far in this assignment if you'd like to (simple_sort_version1, maximum, minimum, etc)

# your function should work perfectly with the following lines of code


def maximum(x,y):
    if x<y:
        return y
    elif y<x:
        return x
    elif x==y:
        return x
    
def minimum(x,y):
    if x<y:
        return x
    elif y<x:
        return y
    elif x==y:
        return x


        

def simple_sort_version2(x,y,z):
    return minimum(minimum(x,y),minimum(y,z)),maximum(minimum(x,y),minimum(y,z)),maximum(maximum(x,y),maximum(y,z))
    


a,b,c = simple_sort_version2(10,20,30)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version2(10,30,20)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version2(30,20,10)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version2(30,20,20)
print (a,b,c) # 20 20 30