import random

list1 = list()
list2 = list([2,3,4])
list3 = list(["red", "green", "blue"])
list4 = list(range(3, 6))
list5 = list("abcd")

list1 = []
list2 = [2,3,4]
list3 = ["red", "green", "blue"]
list4 = [2, "three", 4]

list1 = [2,3,4,1,32]
print(len(list1))
print(max(list1))
print(sum(list1))

random.shuffle(list1)
print(list1)
print(list1[-1])