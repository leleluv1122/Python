import math

def mean(x):
    result = 0
    for i in range(len(x)):
        result += x[i]
    result /= len(x)
    return result

def deciation(x):
    m = mean(x)

    result = 0
    for i in range(len(x)):
        result += ((x[i] - m) ** 2)
    result /= (len(x) - 1)

    total = math.sqrt(result)

    return total


def main():
    s = input("숫자를 입력하세요: ")
    items = s.split()
    lst = [eval(x) for x in items]

    print("평균은 ", format(mean(lst), ".2f"), "입니다.")
    print("표준편차는 ", format(deciation(lst), ".5f"), "입니다.")

main()

# 1.9 2.5 3.7 2 1 6 3 4 5 2