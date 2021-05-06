"""
Marcus Du
5/5/2021
Section 006
Assignment 11
Part 2
"""
import random 
gumballcolors=["red","green","blue"]
class Gumball_Machine:
    def __init__(self,capacity):
        self.moneyamount=0
        self.capacity=capacity
        self.allgumballs=['']*self.capacity
        for i in range(0,len(self.allgumballs)):
            self.allgumballs[i]=random.choice(gumballcolors)
        print("Gumball Machine created with {} random gumballs".format(self.capacity))
    def report(self):
        print("Gumball Machine Report:")
        print("* Gumballs in machine:",len(self.allgumballs))
        print("* Money in machine: $",self.moneyamount)
    def dispense(self,coin):
        if coin!=0.25:
            print("Invalid coin, no gumball will be dispensed")
        else:
            self.moneyamount+=0.25
            random_gumball=random.randint(0,len(self.allgumballs))
            
            try:
                self.allgumballs[random_gumball-1]
            except:
                print("Machine is empty, no gumball will be dispensed")
            else:
                print("Accepting 0.25; Dispensing a {} gumball".format(self.allgumballs[random_gumball-1]))
                del self.allgumballs[random_gumball-1]
        
            
    def count_gumballs_by_type(self,gumballcolor):
        counter=0
        for i in range(0,len(self.allgumballs)):
            if self.allgumballs[i]==gumballcolor:
                counter+=1
        print("There are {} gumballs of type {} in the machine".format(counter,gumballcolor))


machine = Gumball_Machine(5)
machine.report()

machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")

machine.dispense(0.10)
machine.dispense(0.50)
machine.dispense(0.01)

machine.report()

machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")

machine.dispense(0.25)
machine.dispense(0.25)
machine.dispense(0.25)

machine.report()

machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")

machine.dispense(0.25)
machine.dispense(0.25)
machine.dispense(0.25)

machine.report()

machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")


