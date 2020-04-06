number = 43

# 1
if number % 2 == 0:
    even = True
else:
    even = False

print(even)

# 2
even = number % 2 == 0

print(even)

# example
num = 480

if num % 2 == 0:
    print(str(num) + " is even")
else:
    print(str(num) + " is odd")

print("num is even" if(num % 2 == 0) else "number is odd")