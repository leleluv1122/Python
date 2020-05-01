class BMI:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height

    def getBMI(self):
        kil_per_inch = 0.45359237
        meters_per_inch = 0.0254
        bmi = self.__weight * kil_per_inch / ((self.__height * meters_per_inch) * (self.__height * meters_per_inch))
        return round(bmi*100)/100

    def getStatus(self):
        bmi = self.getBMI()
        if bmi < 18.5:
            return "under weight"
        elif bmi < 25:
            return "normal"
        elif bmi < 30:
            return "overweight"
        else:
            return "obese"

    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getWeight(self):
        return self.__weight
    def getHeight(self):
        return self.__height