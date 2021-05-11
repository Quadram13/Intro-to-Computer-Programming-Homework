"""
Marcus Du
5/5/2021
Section 006
Assignment 11
Part 1
"""
class Rectangle:
    
    def __init__(self,width,length,x_pos,y_pos):
        self.wdt=width
        self.len=length
        self.xpos=x_pos
        self.ypos=y_pos
    def get_area(self):
        area=self.wdt*self.len
        return area
    def get_perimeter(self):
        perimeter=(self.wdt+self.len)*2
        return perimeter

rec1=Rectangle(10,15,5,3)
rec2=Rectangle(3,5,15,7)
print("Rectangle #1")
print("* Coordinates: ({}, {})".format(rec1.xpos,rec1.ypos))
print("* Area:",rec1.get_area())
print("* Perimeter:",rec1.get_perimeter())
print()
print("Rectangle #2")
print("* Coordinates: ({}, {})".format(rec2.xpos,rec2.ypos))
print("* Area:",rec2.get_area())
print("* Perimeter:",rec2.get_perimeter())

