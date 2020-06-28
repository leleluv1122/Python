s = input("Enter the integers between 1 and 100: ")
items = s.split()
lst = [eval(x) for x in items]

print("The input numbers are", lst)

d = {}

for i in range(len(lst)):
    if lst[i] in d:
        d[lst[i]] += 1
    else:
        d[lst[i]] = 1

for key, value in sorted(d.items()):
    print(key, "occurs", value, "time")

print("The distinct numbers are", end=' ')

lst2 = []
for key, value in d.items():
    lst2.append(key)
print(lst2, end='')

# 2 5 6 4 3 5 6 5 10 15 34