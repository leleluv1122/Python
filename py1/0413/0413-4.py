for v in range(4, 8):
    print(v)

for v in range(4):
    print(v)

for v in range(3, 9, 2): # 마지막 숫자는 step
    print(v)

for v in range(5, 1, -1):
    print(v)

print("         Multiplication Table")

print("  |", end = '')
for j in range(1, 10):
    print("  ", j, end ='') # end='' 는 enter가 되지않게 하는듯
print()
print("-----------------------------------------")

for i in range(1, 10):
    print(i, "|", end='')
    for j in range(1, 10):
        print(format(i*j, '4d'), end='')
    print()