def add(x, lst = []):
    if not(x in lst):
        lst.append(x)
    return lst

list1 = add(1)
print(list1)
list2 = add(2)
print(list2)

# print(list1)

list3 = add(3, [11,12,13,14])
print(list3)

# print(list1)
list4 = add(4)
print(list4)

# print(list1)

# list1 = list2 = list4 != list3
print(id(list1), id(list2), id(list3), id(list4))