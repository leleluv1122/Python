# weight / ( height*0.1)^2

weight = eval(input("Input your weight: "))
height = eval(input("Input your height: "))

answer = weight / ((height*0.1)**2)
bmi = round(answer * 100, 1)

if bmi <= 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal")
elif bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")

print("Your BMI is " + str(bmi))