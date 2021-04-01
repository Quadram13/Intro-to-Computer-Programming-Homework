"""
Marcus Du
3/16/2021
Section 006
Part 2: Dynamic Gradebook
"""
snum=0
tnum=0
iavg=0 #individual avg score
tavg=0 #total avg score
itot=0
totsum=0
while snum<=0:
    snum=int(input("How many students are in your class? "))
    if snum<=0:
        print("Invalid # of students, try again.")
while tnum<=0:
    tnum=int(input("How many tests are there in your class? "))
    if tnum<=0:
        print("Invalid # of tests, try again.")
for i in range(0,snum):
    print("**** Student #{}****". format(i+1))
    tavg=0
    iavg=0
    itot=0
    
    for j in range(0,tnum):
        score=float(input("Enter score for test #{}: ". format(j+1)))
        if 100<score<0:
            print("Invalid score, try again")
            continue
        itot += score
    print("Average score for student #" +str(i+1), "is",itot/tnum)
    totsum+=itot
    

print("Average score for all students is:",totsum/(tnum*snum))

        

