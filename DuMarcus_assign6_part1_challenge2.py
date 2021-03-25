"""
Marcus Du
3/25/2021
Section 006
Challenge 2
"""
a=5
b=10
c=15
d=20

def maximum(x,y):
    if x<y:
        return y
    elif y<x:
        return x
    
def minimum(x,y):
    if x<y:
        return x
    elif y<x:
        return y
    
ans1=maximum(a,b)
ans2=maximum(a,c)
ans3=maximum(a,d)
print(ans1,ans2,ans3)

ans4 = minimum(d,c)
ans5 = minimum(d,b)
ans6 = minimum(d,a)
print (ans4,ans5,ans6)

ans7 = maximum( maximum(a,b), maximum(c,d) )
print ("The biggest is:", ans7)