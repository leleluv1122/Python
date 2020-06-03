def reverse(lst):
    result = []

    for element in lst:
        result.insert(0, element)
        print(element, result)

    return result

list1 = [1,2,3,4,5,6]
print(list1)
list2 = reverse(list1)
print(list2)

print(id(list1), id(list2))
