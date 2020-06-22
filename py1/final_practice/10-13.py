def eliminateDuplicates(lst):
    result = []

    for i in range(len(lst)):
        a = False
        for j in range(len(result)):
            if lst[i] == result[j]:
                a = True
        if a == False:
            result.append(lst[i])

    return result

def main():
    s = input("10개의 숫자를 입력하세요: ")
    items = s.split()
    lst = [eval(x) for x in items]

    lst2 = eliminateDuplicates(lst)

    for i in range(len(lst2)):
        print(lst2[i], end=' ')

main()

# 1 2 3 2 1 6 3 4 5 2