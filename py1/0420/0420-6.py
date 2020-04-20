# Example 1
globalVar = 1
def f1():
    localVar = 2
    print(globalVar)
    print(localVar)

f1()
print(globalVar)
# print(localVar) # Out of scope, This gives an error

print()


# Example 2
x = 1
def f1():
    x = 2
    print(x)
f1()
print(x)

print()



# Example 3
x = eval(input("Enter a number: "))
if (x > 0):
    y=4
print(y) # This gives an error if y is not created

print()


# Example 4
sum = 0
for i in range(0, 5):
    sum += i
print(i)

print()


# Example 5
x = 1
def increase():
    global x
    x = x + 1
    print(x)
increase() # 2
print(x) # 2