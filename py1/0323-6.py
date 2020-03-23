# input Type likes 10,20,30
num1, num2, num3 = eval(input("Enter 3 numbers:"))

average = (num1+num2+num3)/3
print(average)

num1, num2 = num2, num1
print(num1)
print(num2)

print("5 // 3 =", 5//3)
print("5 % 3 =", 5%3)