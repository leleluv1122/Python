s1 = str()
s2 = str("Welcome")
print(len(s2))
print(max(s2)) # ASCII가 제일 큰값
print(min(s2))

s1 = "Welcome"
s2 = "Python"
s3 = s1 + " to " + s2
print(s3)

s4 = 2 * s1
print(s4)

print(s1[3:6]) # 3~5 6은포함X

print('W' in s1)
print('X' in s1)

print(s1[-1]) # 제일 뒤에있는 값
print(s1[-3:-1]) # 뒤에서 3번째 부터 2까지.

print("come" in s1)
print("come" not in s1 )