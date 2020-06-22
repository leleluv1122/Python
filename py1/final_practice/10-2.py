def main():
    s = input("점수를 입력하세요: ")
    items = s.split()
    lst = [eval(x) for x in items]

    for i in range(len(lst)-1, -1, -1):
        print(lst[i], end=' ')

main()

# 2 5 6 5 4 3 23 43 2