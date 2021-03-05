"""
Marcus Du
2/3/2021
Section 006
Problem #1: Variables and Print Statements
"""

classname='Introduction to Computer Programming' #this variable is the class name


test1avg,test2avg,test3avg=95,76,87

"""
the line above stores the values for the avaerages of 3 tests
"""

print('Average Test Scores For ',classname,':',sep='"')
"""
the line above prints the statement describing what values are displayed, made use
of sep because the string for class name didnt have quotation marks on the
assignment page, and putting '"' in between the string above and the variable
would've resulted in the formatting being off
"""
print('- Test #1:',test1avg)
print('- Test #2:',test2avg)
print('- Test #3:',test3avg)
"""
prints the 3 average values, no special formatting required other
"""
