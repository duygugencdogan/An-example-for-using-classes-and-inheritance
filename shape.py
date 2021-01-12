
pi = 3.1415  #pi 

class Shape():
    def __init__(self,shapename,edge1):
        self.shapename = shapename
        self.edge1 = edge1
        print("This shape is a {}.".format(self.shapename))


class ScalaneTriangle(Shape):
    def __init__(self,shapename,edge1,edge2,edge3):
        self.shapename = shapename
        self.edge1 = edge1
        self.edge2 = edge2
        self.edge3 = edge3

    def get_perimeter(self):
        print(self.edge1 + self.edge2 + self.edge3)  # (a+b+c)

    def get_area(self):   
        s = (self.edge1 + self.edge2 + self.edge3)/2
        print((s*(s-self.edge1)*(s-self.edge2)*(s-self.edge3))**(1/2))   # square of s*(s-a)*(s-b)*(s-c) 


class Rectangle(Shape):
    def __init__(self,shapename,edge1,edge2):
        self.shapename = shapename
        self.edge1 = edge1
        self.edge2 = edge2
    def get_perimeter(self):
        print(2*(self.edge1 + self.edge2))  #2*(a+b)

    def get_area(self):
        print(self.edge1 * self.edge2) #2*a*b

class Square(Shape):
    def get_perimeter(self):
        print(4 * self.edge1)  # 4 edges

    def get_area(self):
        print(self.edge1**2) # a square root

class EquilateralTriangle(Shape):
    def get_perimeter(self):
        print(3 * self.edge1)     #3 edges
    def get_area(self):
        print((self.edge1**2)*(3**(1/2))/4)  #a square root * 3 divided by 4

class Circle(Shape):
    def get_perimeter(self):
        radius = self.edge1   #radius is a variable here.
        print(2* pi * radius)  # 2 pi r

    def get_area(self):
        print(pi*(radius**2)) #  pi r kare

print("-"*30)
#Creating an object 
rectangle1 = Rectangle("Rectangle",5,20)
rectangle1.get_perimeter()
rectangle1.get_area()

print("-"*30)
#Creating an object
square1 = Square("Square",10)
square1.get_perimeter()
square1.get_area()

print("-"*30)
#Creating an object
circle1 = Circle("Circle",5)
circle1.get_perimeter()
circle1.get_area()

print("-"*30)
#Creating an object
equilateralTriangle1 = EquilateralTriangle("Equilateral Triangle",10)
equilateralTriangle1.get_perimeter()
equilateralTriangle1.get_area()

print("-"*30)
#Creating an object
scalaneTriangle1 = ScalaneTriangle("Scalane Triangle",5,12,13)  # 5,12,13 is also a Right Triangle.
scalaneTriangle1.get_perimeter()
scalaneTriangle1.get_area()
