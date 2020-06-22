def sumMajorDiagonal(m):
    total = 0
    for i in range(4):
        for j in range(4):
            if i == j:
                total += m[i][j]
    return total




def main():
    arr = []
    for i in range(4):
        arr.append([])
        s = input("4x4 행렬의 행 "+ str(i) +" 번에 대한 원소를 입력하세요: ")
        items = s.split()
        arr[i] = [eval(x) for x in items]

    print("주대각선에 포함된 원소의 합계는", str(sumMajorDiagonal(arr)), "입니다. ")


main()

# 1 2 3 4
# 2 6.5 7 8
# 9 10 11 12
# 13 14 15 16