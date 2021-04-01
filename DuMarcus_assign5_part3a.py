"""
Marcus Du
3/16/2021
Section 006
Part 3a: Prime Number Finder
"""
tnum=0
while tnum<=0:
    tnum=int(input("Enter a positive number to test: "))
if tnum==1:
    print("1 is technically not a prime number.")
for i in range(2,tnum):
    if tnum%i!=0:
        print(str(i),"is NOT a divisor of",tnum, " ... continuing")
        
    elif tnum%i==0:
        print(str(i),"is a divisor of",tnum," ... stopping")
        print()
        print(str(tnum),"is not a prime number")
        break
   
print("{} is a prime number". format(tnum))
        