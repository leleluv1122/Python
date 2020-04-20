def nPrintLn(message, n):
    for i in range(0, n):
        print(message)

# nPrintLn(4, "Computer Science") # wrong
nPrintLn("Computer Science", 4)
nPrintLn(n=4, message="Computer Science")

def main():
    x = 1
    print("Before the call, x is", x)
    increment(x)

    print("After the call, x is", x)

def increment(n):
    n += 1
    print("\tn inside the function is", n)

main()