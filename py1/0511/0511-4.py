def main():
    s = input("Enter a string: ").strip() # space 없애기

    if isPalindrom(s):
        print(s, "is a Palindrom")
    else:
        print(s, "is not a Palindrom")

def isPalindrom(s):
    low = 0
    high = len(s) - 1

    while low < high:
        if s[low] != s[high]:
            return False

        low += 1
        high -= 1

    return True

main()