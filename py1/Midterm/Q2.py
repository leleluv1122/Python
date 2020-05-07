import math

class Triangle: # 삼각형
    def __init__(self, mitbyeon, nopii):
        self.__mitbyeon = mitbyeon # 밑변
        self.__nopii = nopii # 높이

    def getArea(self):
        r = (self.__mitbyeon * self.__nopii) / 2
        return r

class Square: # 정사각형
    def __init__(self, side):
        self.__side = side

    def getArea(self):
        r = self.__side**2
        return r

class Circle: # 원
    def __init__(self, radius):
        self.__radius = radius # 반지름

    def getArea(self):
        r = self.__radius**2 * math.pi
        return r

def main():
    t = Triangle(10,30)
    print(format(t.getArea(), ".4f"))

    s = Square(20)
    print(format(s.getArea(), ".4f"))

    c = Circle(30)
    print(format(c.getArea(), ".4f"))

main()
