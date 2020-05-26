list1 = ["green", "red", "blue"]
list2 = ["red", "blue", "green"]

print(list2 == list1)
print(list2 != list1)
print(list2 > list1) # 처음에 나오는 거의 ascii비교
print(list2 < list1)
print(list2 <= list1)

list1 = [2,3,4,1,32,4]
list1.append(19)
print(list1)
print(list1.count(4))
list2 = [99,54]
list1.extend(list2)
print(list1)
print(list1.index(4))

list1.insert(1, 25)
print(list1)