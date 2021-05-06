"""
Marcus Du
5/5/2021
Section 006
Assignment 11
Part 3
"""
class Smartphone:

	# construct a new Smartphone
	# smartphones need to keep track of how much space they have left (integer)
	# they also need to keep track of their name (string)
	# smartphones will need some kind of internal system to keep track of all of 
	# the apps that are installed, along with their size.  a list or a dictionary
	# would be useful here.
	# when a phone is constructed the 'report' method should be called (see below)
	# this method returns nothing and simply prints the desired output to the user
	def __init__(self, capacity, name):
            self.name=name
            self.capacity=capacity
            self.applist=dict()
            self.numapps=0
            print("Smartphone created!")
            self.capacityused=0
            self.report()
            
            
            
        

        




	# add a new app to the smartphone given an appname (string) and an appsize (integer)
	# if the app is already installed, reject it.  if the phone cannot hold any additional
	# apps because the capacity has been reached, reject it.
	# this method returns nothing and simply prints the desired output to the user
	def add_app(self, appname, appsize):
            current_capacity=int(self.get_available_space())
            if appname in self.applist:
                print("Cannot install app, app is already installed")
            elif appsize>current_capacity:
                print("Cannot install app, no available space")
            else:
                self.applist[appname]=appsize
                self.capacityused+=int(appsize)
                self.numapps+=1
                print("App installed!")


	# removes an app from the phone based on appname (string)
	# if the app is not installed, reject it
	# this method returns nothing and simply prints the desired output to the user
	def remove_app(self, appname):
            if appname in self.applist:
                self.capacityused+=-(self.applist[appname])
                del self.applist[appname]
                self.numapps+=-1
                print("App deleted")

            else:
                print("Cannot remove app, app does not exist")


	# checks to see if an app is installed based on appname (string)
	# returns True if the app is installed, False if it is not
	def has_app(self, appname):
            if appname in self.applist:
                return True
            else:
                return False
            


	# returns the current space available on the phone (integer)
	def get_available_space(self):
            
            capacityfree=self.capacity-self.capacityused
            return capacityfree


	# prints a detailed report that describes the following:
	# Name of phone
	# Capacity of phone
	# Available space
	# # of apps installed
	# a listing of all apps installed, in alphabetical order, with their sizes
	# this method returns nothing and simply prints the desired output to the user
	def report(self):
            print("Name:",self.name)
            print("Capacity: {} out of {} GB used".format(self.capacityused,self.capacity))
            print("Available space:",self.get_available_space(),"GB")
            print("Apps installed:",self.numapps)
            if self.numapps>0:
                for key in self.applist:
                    print("* {} is using {} GB".format(key,self.applist[key]))

        


choose_size=int(input("Size of your new smartphone (32, 64 or 128 GB): "))
choose_name=input("Smartphone name: ")
yourphone=Smartphone(choose_size,choose_name)
q=False
print()
while q==False:
    wtd=input("(r)eport, (a)dd app, r(e)move app or (q)uit: ")
    if wtd=="r":
        yourphone.report()
    elif wtd=="a":
        added_app=input("App name to add: ")
        added_app_size=int(input("App size in GB: "))
        yourphone.add_app(added_app,added_app_size)
    elif wtd=="e":
        app_2remove=input("App name to remove: ")
        yourphone.remove_app(app_2remove)
    elif wtd=="q":
        q=False
        print("Goodbye!")
    else:
        print("Invalid input, please try again")
