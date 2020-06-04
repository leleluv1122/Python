# 삽입정렬 ( Insertion Sort )

def insertionSort(lst):
    for i in range(1, len(lst)):
        currentElement = lst[i]
        k = i - 1
        while k >= 0 and lst[k] > currentElement:
            lst[k + 1] = lst[k]
            k -= 1

        lst[k + 1] = currentElement

lst = [1, 9, 4.5, 10.6, 5.7, -4.5]
insertionSort(lst)
print(lst)