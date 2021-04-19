"""
Marcus Du
4/15/2021
Section 006
Part 2: Fast Food Restaurant
"""

product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]
product_quantity=[10,5,20]
cont=True






while cont==True:

    wtd=input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
    
    while wtd=="s":
        pname=input("Enter a product name: ")
        if pname in product_names:
            print('We sell "{}" for {} per unit'.format(pname,product_costs[product_names.index(pname)]))
            print()
        else:
            print("Sorry, we don't sell {}".format(pname))
            print()
        wtd=input("(s)earch, (l)ist, (a)dd or (q)uit: ")
            
    while wtd=="q":
        print("See you soon!")
        cont==False
        
        

    while wtd=="l":
        print(format('Product', '<15s'),format("Price",'<8s'),"Quantity")
        for i in range(0,len(product_names)):
            print(format(str(product_names[i]), '<15s'),format(str(product_costs[i]), '<8s'),product_quantity[i])
        print()
        wtd=input("(s)earch, (l)ist, (a)dd or (q)uit: ")

    while wtd=="a":
        newprod=input("Enter a new product name: ")
        while newprod in product_names:
            print("Sorry, we already sell that product. Try again.")
            newprod=input("Enter a new product name: ")
        else:
            product_names.append(newprod)
        newprodprice=float(input("Enter a product cost: "))
        while newprodprice<=0:
            print("Invalid cost. Try again.")
            newprodprice=float(input("Enter a product cost: "))
        else:
            product_costs.append (newprodprice)
        
        newprodquant=int(input("How many of these products do we have? "))
        while newprodquant<=0:
            print("Invalid quantitiy. Try again.")
            newprodquant=int(input("How many of these products do we have? "))
        else:
            product_quantity.append (newprodquant)
        print()
        wtd=input("(s)earch, (l)ist, (a)dd or (q)uit: ")


    

    
