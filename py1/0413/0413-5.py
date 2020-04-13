n1, n2 = eval(input("두 수 입력하기: "))

if n1 < n2:
    n1, n2 = n2, n1

gcd = 1

for i in range(2, n1):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i

print(n1, "and", n2, ": ", gcd)