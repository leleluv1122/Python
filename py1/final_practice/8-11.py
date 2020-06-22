def reverse(s):
    for i in range(len(s)-1, -1, -1):
        print(s[i], end='')

def main():
    reverse("Welcome To Python")

main()