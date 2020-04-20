def decimalToHex(decimalValue):
    hex = ""

    while decimalValue != 0:
        hexValue = decimalValue % 16 # 나머지
        hex = toHexChar(hexValue) + hex
        decimalValue = decimalValue // 16 # 몫

    return hex

def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else: # 10 <= hexValue <= 15
        return chr(hexValue - 10 + ord('A'))

def main():
    decimalValue = eval(input("Enter a decimal number: "))

    print("The hex number for decimal", decimalValue, "is", decimalToHex(decimalValue))

main()