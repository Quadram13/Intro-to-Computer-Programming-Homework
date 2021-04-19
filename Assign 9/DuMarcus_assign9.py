"""
Marcus Du
4/19/2021
Section 006
Part 1
"""
filename=input("Enter a class file to grade (i.e. class1 for class1.txt): ")
file_actual=filename+".txt"
#try:
file_object=open("class1.txt","r")
alldata=file_object.read()

print(alldata)

file_object.close()



"""except:
    print("File cannot be found. ")
else:
    print("Successfully opened class1.txt")
"""