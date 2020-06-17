import math

class Circle():
    def __init__(self, radius):
        super().__init__()
        self.setRedius(radius)

    def getRadius(self):
        return self.__radius

    def setRedius(self, radius):
        if radius < 0:
            raise RuntimeError("Nagative radius")
        else:
            self.__radius = radius

    def getArea(self):
        return self.__radius * self.__radius * math.pi

    def getDiameter(self):
        return 2 * self.__radius

    def getParimeter(self):
        return 2 * self.__radius * math.pi

    def printCircle(self):
        print(self.__str__() + " radius: " + str(self.__radius))

def main():
    try:
        c1 = Circle(5)
        print("c1's area is", c1.getArea())
        c2 = Circle(-5)
        print("C2's area is", c2.getArea())
        c3 = Circle(0)
        print("c3's area is", c3.getArea())
    except RuntimeError as ex:
        print("Invalid radius", ex)

main()