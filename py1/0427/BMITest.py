from BMI import BMI

def main():
    b = BMI("seuni", 24, 167, 53)
    print("The BMI for", b.getName(), "is", b.getBMI(), b.getStatus())
    b2 = BMI("peter",50,215,70)
    print("The BMI for", b2.getName(), "is", b2.getBMI(), b2.getStatus())

main()
# 먼가 이상함 ..