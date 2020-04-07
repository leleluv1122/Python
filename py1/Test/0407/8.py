# Dictionary
# key:value

x = {
    "name": "스니",
    "age" : 24,
}

print(x)
print(x["name"])
print(x["age"])

x = {
    0: "Seuni",
    1: "Hello",
    "age": 20,
}

print(x[0])
print(x[1])
print(x["age"])

print("age" in x) # age라는 key가 x에 있나유?
print("name" in x)

print(x.keys())
print(x.values())

for key in x:
    print("key: " +str(key))
    print("value: " + str(x[key]))

x[0] = "스니"
print(x)

x["school"] = "한빛"
print(x)