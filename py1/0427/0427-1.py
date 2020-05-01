# Object Oriented Programming
import math

class Circle:
    def __init__(self, radius = 1):
        self.radius = radius

    def getParameter(self):
        return 2 * self.radius * math.pi

    def getArea(self):
        return self.radius * self.radius * math.pi

    def setRadius(self, radius):
        self.radius = radius

# from Circle import Circle

def main():
    c1 = Circle()
    print("radius", c1.radius, "is" ,c1.getArea())

    c = Circle(3)
    print(c.getParameter())

    c.radius = 125
    print(c.getArea())

main()