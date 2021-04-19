"""
Marcus Du
4/19/2021
Section 006
Part 1
"""
file_for_grading=input("Enter a class file to grade (i.e. class1 for class1.txt): ")
try:
    open(str(file_for_grading),"r")
    """
except:
    print("File cannot be found.")
else:
    print("Successfully opened class1.txt")


"""