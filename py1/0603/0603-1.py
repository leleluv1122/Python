list1 = [1,2]
list2 = [3,4,5]

print(id(list1))
print(id(list2))

list2 = list1

print(id(list2)) # 포인트가 list1을 가리킴

list1 = [0,1,2,3,4,5,6]
list2 = [] + list1 # 깊은복사느낌
list1[0] = 7
print(list1)
print(list2)