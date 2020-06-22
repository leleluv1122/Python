def sumColumn(m, columnIndex):
    total = 0
    for i in range(3):
        for j in range(4):
            if j == columnIndex:
                total += m[i][j]
    return total

def main():
    arr = []
    for i in range(3):
        arr.append([])
        s = input("3x4 행렬의 행 "+ str(i) +" 번에 대한 원소를 입력하세요: ")
        items = s.split()
        arr[i] = [eval(x) for x in items]

    for i in range(4):
        print("열 "+str(i) + " 번 원소의 총 합은",format(sumColumn(arr, i), ".1f") ,"입니다.")



main()


# 1.5 2 3 4
# 5.5 6 7 8
# 9.5 1 3 1