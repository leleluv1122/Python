def binaryToDecimal(binaryString):
    a = 1
    result = 0
    for i in range(len(binaryString)-1, -1, -1):
        result += int(binaryString[i]) * a
        a *= 2

    return result


def main():
    print(binaryToDecimal("10001"))

main()