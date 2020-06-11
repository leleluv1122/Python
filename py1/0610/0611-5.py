s1 = {1, 2, 4}
s2 = {1, 3, 5}
print(s1.union(s2))
print(s1 | s2)

print(s1.intersection(s2)) # 공통적으로 들어가있는 숫자
print(s1 & s2)

print(s1.difference(s2))
print(s1 - s2)

print(s1.symmetric_difference(s2))
print(s1 ^ s2)