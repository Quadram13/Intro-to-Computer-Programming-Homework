"""
Marcus Du
2/25/2021
Section 006
Problem #1: Valid Triangle Tester
"""
p_1x=float(input("Please enter Point #1 - x position: "))
p_1y=float(input("Please enter Point #1 - y position: "))
p_2x=float(input("Please enter Point #2 - x position: "))
p_2y=float(input("Please enter Point #2 - y position: "))
p_3x=float(input("Please enter Point #3 - x position: "))
p_3y=float(input("Please enter Point #3 - y position: "))

side_1=((p_1x-p_2x)**2+(p_1y-p_2y)**2)**0.5
side_2=((p_2x-p_3x)**2+(p_2y-p_3y)**2)**0.5
side_3=((p_3x-p_1x)**2+(p_3y-p_1y)**2)**0.5

side_1f=format(side_1, '.2f')
side_2f=format(side_2, '.2f')
side_3f=format(side_3, '.2f')

if (side_1+side_2)>side_3 and (side_2+side_3)>side_1 and (side_3+side_1)>side_2 :
    
    print("The length of each side of your test shape is:")
    print("Side 1:",side_1f)
    print("Side 2:",side_2f)
    print("Side 3:",side_3f)
    print("This is a valid triangle!")
else:
    print("The length of each side of your test shape is:")
    print("Side 1:",side_1f)
    print("Side 2:",side_2f)
    print("Side 3:",side_3f)
    print("This is not a valid triangle!")
