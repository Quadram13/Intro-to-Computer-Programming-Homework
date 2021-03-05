"""
Marcus Du
2/17/2021
Section 006
Problem #2: Grade Calculator
"""
name=input("Hi! What is your name?")
your_class=input("What is your class")
test_weighting=float(input("How much are tests worth in this class(Please enter as a decimal, not a percentage)"))
test_1=int(input("Please input your first test score"))
test_2=int(input("Please input your second test score"))
test_3=int(input("Please input your third test score"))
test_avg=(test_1+test_2+test_3)/3
print("Your test average is",test_avg)
hw_weighting=float(input("How much are homework assignments worth in this class(Please enter as a decimal, not a percentage)"))
hw_1=int(input("Please input your first homework score"))
hw_2=int(input("Please input your second homework score"))
hw_3=int(input("Please input your third homework score"))
hw_avg=(hw_1+hw_2+hw_3)/3
print("Your homework average is",hw_avg)
yourclassgradeweighted=(test_avg*test_weighting)+(hw_avg*hw_weighting)
print()
print("Thanks",name,"Your final score in",your_class,"is",yourclassgradeweighted)
