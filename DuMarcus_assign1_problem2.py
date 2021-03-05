"""
Marcus Du
2/3/2021
Section 006
Problem #2: Using the print function
"""
name1=input("Please enter name #1: ")
name2=input("Please enter name #2: ")
name3=input("Please enter name #3: ")
"""
Above lines ask for the 3 names that will be ordered in this program
"""
print()
print("Here are your names in every possible order:")
print("--------------------------------------------")
print()
print("1.",end = " ")
print(name1,name2,name3,sep=", ")
print()
print("2.",end=" ")
print(name1,name3,name2,sep=", ")
print()
print("3.",end=" ")
print(name2,name1,name3,sep=", ")
"""
Above lines format the 3 names so that they are in different orders, but on the same line
"""
print()
print("4.",name2)
print(name3)
print(name1)
print()
print("5.",name3)
print(name2)
print(name1)
print()
print("6.",name3)
print(name1)
print(name2)
"""
Above lines separate the three names into different lines, with each list of 3 separated by a line break
"""
