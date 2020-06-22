def main():
    txt = input("파일명을 입력하세요: ")
    infile = open(txt, "r")
    s = infile.readline()
    print(s)
    items = s.split()
    lst = [eval(x) for x in items]

    print(len(lst), "개의 점수가 있습니다.")

    total = 0
    for i in range(len(lst)):
        total += lst[i]
    print("총 점수는 " + str(total) + " 입니다. ")

    mean = total / len(lst)
    print("평균 점수는", format(mean, ".2f"), "입니다.")

    infile.close()

main()