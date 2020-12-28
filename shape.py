
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

    def get_perimeter(self,edge1,edge2,edge3):
        print(self.edge1 + self.edge2 + self.edge3)  # (a+b+c)

    def get_area(self,edge1,edge2,edge3):   
        s = (self.edge1 + self.edge2 + self.edge3)/2
        print((s*(s-self.edge1)*(s-self.edge2)*(s-self.edge3))**(1/2))   # square of s*(s-a)*(s-b)*(s-c) 


class Rectangle(Shape):
    def __init__(self,shapename,edge1,edge2):
        self.shapename = shapename
        self.edge1 = edge1
        self.edge2 = edge2
    def get_perimeter(self,edge1,edge2):
        print(2*(self.edge1 + self.edge2))  #2*(a+b)

    def get_area(self,edge1, edge2):
        print(self.edge1 * self.edge2) #2*a*b

class Square(Shape):
    def get_perimeter(self,edge1):
        print(4 * self.edge1)  # 4 edges

    def get_area(self,edge1):
        print(self.edge1**2) # a square root

class EquilateralTriangle(Shape):
    def get_perimeter(self,edge1):
        print(3 * self.edge1)     #3 edges
    def get_area(self,edge1):
        print((self.edge1**2)*(3**(1/2))/4)  #a square root * 3 divided by 4

class Circle(Shape):
    def get_perimeter(self,radius):
        radius = self.edge1   #radius is a variable here.
        print(2* pi * radius)  # 2 pi r

    def get_area(self, radius):
        print(pi*(radius**2)) #  pi r kare


#Creating an object 
rectangle1 = Rectangle("Rectangle",5,20)
rectangle1.get_perimeter(5,20)
rectangle1.get_area(5,20)

#Creating an object
square1 = Square("Square",10)
square1.get_perimeter(10)
square1.get_area(10)

#Creating an object
circle1 = Circle("Circle",5)
circle1.get_perimeter(5)
circle1.get_area(5)

#Creating an object
equilateralTriangle1 = EquilateralTriangle("Eşkenar Üçgen",10)
equilateralTriangle1.get_perimeter(10)
equilateralTriangle1.get_area(10)

#Creating an object
scalaneTriangle1 = ScalaneTriangle("Çeşitkenar Üçgen",5,12,13)  # 5,12,13 aynı zamanda bir dik üçgen
scalaneTriangle1.get_perimeter(5,12,13)
scalaneTriangle1.get_area(5,12,13)
