print(format(57.467657, '10.2f'))
print(format(12345678.923, '10.2f'))
print(format(57.4, '10.2f'))
print(format(57, '10.2f'))

# 뒤에 둘째자리는 승
print(format(57.467657, '10.2e'))
print(format(0.0033923, '10.2e'))
print(format(57.4, '10.2e'))
print(format(57, '10.2e'))

print(format(0.53457, '10.2%'))
print(format(0.003923, '10.2%'))
print(format(7.4, '10.2%'))
print(format(57, '10.2%'))

print(format(57.467657, '10.2f'))
print(format(57.467657, '<10.2f')) #왼쪽정렬

print(format(59832, '10d'))
print(format(59832, '<10d')) # 10진법 / 10자리
print(format(59832, '10x'))
print(format(59832, '<10x')) # 16진법
print(format("Welcome to Python", '20s'))
print(format("Welcome to Python", '<20s'))
print(format("Welcome to Python", '>20s'))