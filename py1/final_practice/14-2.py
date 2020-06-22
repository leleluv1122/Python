def main():
    s = input("숫자를 입력하세요: ")
    items = s.split()
    lst = [eval(x) for x in items]

    d = {}

    for i in range(len(lst)):
        if lst[i] in d:
            d[lst[i]] += 1
        else:
            d[lst[i]] = 1
    max_num = max(d.values())
    max_lst = []

    for key, value in d.items():
        if value == max_num:
            max_lst.append(key)

    for i in range(len(max_lst)):
        print(max_lst[i], end=' ')

main()

# 2 3 40 3 5 4 -3 3 3 2 0
# 9 30 3 9 3 2 4