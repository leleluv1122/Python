# List
x = [1, 2, 3, 4]
y = ["hello", "world"]
z = ["hello", 1,2,3]

print(x + y)
print(z)

x = [4,2,1,3]
print(x[0])

z = sum(x)
print(z)

y = sorted(x)
print(y)

x[3] = 10
print(x)

num_elements = len(x)
print(num_elements)


x = [4,2,3,1]
y = ["hello", "there"]

for n in x:
    print(n)
for c in y:
    print(c)

print(x.index(3)) # 3이란게 몇번째에 있는지
print(y.index("hello"))
print("hello" in y) # hello가 y에 있는가? True
print("bye" in y)

if "hello" in y:
    print("Hello 가 있다=_=")