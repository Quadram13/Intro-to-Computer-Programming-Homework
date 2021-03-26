"""
Marcus Du
3/4/2021
Section 006
Program 3: Arrows
lv=whether the number of columns is valid
dv=whether the inputed directed is correct
c_n=numbers of columns to the midpoint
ww=which way the arrow is pointing
c_p=current point, will be adding 1 every time the program moves onto the next line
sp=number of spaces
passed=whether
"""


lv=False
dv=False
c_n=0
ww=""
c_p=1
sp=""
passed=False
while lv==False:
    c_n=int(input("How many columns?"))
    if c_n<=0:
        print("Invalid entry, try again!")
        continue
    else:
        lv=True

while dv==False:
    ww=input("Direction? (l)eft or (r)ight:")
    if ww!="l"and ww!="r":
        print("Invalid entry, try again!")
        continue
    else:
        dv=True

if ww=="r":
    for c_p in range(1,c_n+1):
        sp=' '*(c_p-1)
        print(sp,"*",sep='')
    for c_p in range(c_n+1,(c_n*2)):
        sp=' '*(((c_n*2)-1)-c_p)
        print(sp,"*",sep='')
elif ww=="l":
    for c_p in range(1,c_n+1):
        sp=' '*(c_n-c_p)
        print(sp,"*",sep='')
    for c_p in range(c_n+1,(c_n*2)):
        sp=' '*(c_p-c_n)
        print(sp,"*",sep='')









