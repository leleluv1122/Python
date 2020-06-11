s1 = {1, 2, 4}
s2 = {1, 4, 5, 2, 6}
s1.add(6)
print(s1)

print(len(s1))
print(max(s1))
print(min(s1))
print(sum(s1))
print(3 in s1)

s1.remove(4)
print(s1)

print(s1.issubset(s2)) # 부분집합
print(s2.issuperset(s1)) # 상위집합