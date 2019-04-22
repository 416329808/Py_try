import math
class Shape:
    def Area(self):
        pass
    def Perimeter(self):
        pass

class Triangle(Shape):
    a = 0
    b = 0
    c = 0
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def Area(self):
        p = (self.a+self.b+self.c)/2
        x = p*(p-self.a)*(p-self.b)*(p-self.c)
        area=x**0.5
        print("该三角形的面积为：",area)
    def Perimeter(self,):
        print("该三角形周长为：",self.a+self.b+self.c)

class Rectangle(Shape):
    long = 6
    width = 6
    def __init__(self,l,w):
        self.long=l
        self.width=w
    def Area(self):
        print("该矩形面积为:",self.long*self.width)
    def Perimeter(self):
        print("该矩形周长为：",(self.long+self.width)*2)

class Circle(Shape):
    radius=0
    def __init__(self,r):
        self.radius=r
    def Area(self):
        print("该圆形的面积为:",self.radius*self.radius*math.pi)
    def Perimeter(self):
        print("该圆形的周长为", 2*3.14*self.radius)
t = Triangle(3, 4, 5)
t.Area()
t.Perimeter()
r = Rectangle(7, 8)
r.Area()
r.Perimeter()
c = Circle(6)
c.Area()
c.Perimeter()
