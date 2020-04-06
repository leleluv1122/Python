import random

number1 = random.randint(1, 9)
number2 = random.randint(1, 9)

if number1 < number2:
    number1, number2 = number2, number1 # Swap

answer = eval(input("What is " + str(number1) + " - " + str(number2) + " ? "))

if number1-number2 == answer:
    print("correct")
else:
    print("wrong.. answer is " + str(number1- number2))
