"""
Marcus Du
3/16/2021
Section 006
Part 1: Pizza Party

"""
bgt=float(input("Enter budget for your party: "))
s_cost=float(input("Cost per slice of pizza: "))
p_cost=float(input("Cost per whole pie of pizza(8 slices): "))
ppl=int(input("How many people will be attending your party: "))
ttlslc=0
slcnt=0
i=1
while i<ppl:
    slcnt=int(input("Enter number of slices for person #{}: ". format(i)))
    if slcnt<=0:
        print("Not a valid entry, try again!")
        slcnt=0
    else:
        ttlslc=slcnt+ttlslc
        i=i+1
        
pnum=ttlslc//8 
slnum=ttlslc%8
tcst=pnum*p_cost+slnum*s_cost
if bgt>tcst:
    print("You should purchase",pnum,"pies and",slnum,"slices")
    print("Your total cost will be",tcst)
    print("You will still have",bgt-tcst,"left after your order")
elif bgt==tcst:
    print("You should purchase",pnum,"pies and",slnum,"slices")
    print("Your total cost will be",tcst)
    print("You will have no money left after your order.")
else:
    print("Your order cannot be completed.")
    print("You would need to purchase",pnum,"pies and",slnum,"slices")
    print("This would put you over budget by",tcst-bgt)