"""
Marcus Du
2/17/2021
Section 006
Problem #3: Minecraft Distance Calculator
"""


b1x=int(input("Block #1's x component"))
b1y=int(input("Block #1's y component"))
b1z=int(input("Block #1's z component"))
b2x=int(input("Block #2's x component"))
b2y=int(input("Block #2's y component"))
b2z=int(input("Block #2's z component"))

if b1x<b2x<0:
    x_d=abs(b1x)-abs(b2x)
elif b2x<b1x<0:
    x_d=abs(b2x)-abs(b1x)
elif b1x<0 and b2x>=0:
    x_d=b2x+abs(b1x)
elif b1x>=0 and b2x<0:
    x_d=b1x+abs(b2x)
elif b2x>=0 and b1x<0:
    x_d=b2x+abs(b1x)
else:
    x_d=abs(b2x-b1x)
    
if b1y<b2y<0:
    y_d=abs(b1y)-abs(b2y)
elif b2y<b1y<0:
    y_d=abs(b2y)-abs(b1y)
elif b1y<0 and b2y>=0:
    y_d=b2y+abs(b1y)
elif b1y>=0 and b2y<0:
    y_d=b1y+abs(b2y)
elif b2y>=0 and b1y<0:
    y_d=b2y+abs(b1y)
else:
    y_d=abs(b2y-b1y)
    

if b1z<b2z<0:
    z_d=abs(b1z)-abs(b2z)
elif b2z<b2z<0:
    z_d=abs(b2z)-abs(b1z)
elif b1z<0 and b2x>=0:
    z_d=b2z+abs(b1z)
elif b1z>=0 and b2z<0:
    z_d=b1z+abs(b2z)
elif b2z>=0 and b1z<0:
    z_d=b2z+abs(b1z)
else:
    z_d=abs(b2z-b1z)
"""
negative values would throw off calulation if i had just used the one condition b2x-b1x and so on

In hindsight I couldve used loops to shorten this but I watched the module after I completed this code
"""



stlinedistform=((x_d**2)+(y_d**2)+(z_d**2))**(1/2)
"""
what got me stuck on this one so long was that i had forgotten to add the parenteses around the 1/2
"""

print("The x distance is",x_d)
print("The y distance is",y_d)
print("The z distance is",z_d)
print("The stright line distance in 3 dimensions is",stlinedistform)
