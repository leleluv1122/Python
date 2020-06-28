import random

lst = []

for i in range(1000):
    a = random.randint(1, 6)
    lst.append(a)

d = {}

for i in range(len(lst)):
    if lst[i] in d:
        d[lst[i]] += 1
    else:
        d[lst[i]] = 1

for key, value in sorted(d.items()):
    print("주사위가",key,"인 경우는", value,"번")