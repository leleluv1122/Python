def score(num, max_num):
    result = max_num - num

    if result <= 10:
        return "A"
    elif 10 < result <= 20:
        return "B"
    elif 20 < result <= 30:
        return "C"
    elif 30 < result <= 40:
        return "D"
    else:
        return "F"

def main():
    s = input("점수를 입력하세요: ")
    items = s.split()
    lst = [eval(x) for x in items]

    max_num = 0
    for i in range(len(lst)):
        if max_num < lst[i]:
            max_num = lst[i]

    for i in range(len(lst)):
        print("학생 " + str(i) + "의 점수는 " + str(lst[i]) + " 이고 성적은 " + str(score(lst[i], max_num)) + " 입니다.")

main()

# 40 55 70 58