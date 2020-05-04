import math

a, b, c = eval(input("a, b, c를 입력하세요: "))
d = b**2 - 4*a*c
if d >= 0:
    e = math.sqrt(d)

# print(d)
if d > 0:
    r1 = (abs(b) + e) / (2 * a)
    r2 = ((0 - b) - e) / (2 * a)
    print("실근은 ", format(r1,".6f"), "이고 ", format(r2,".5f") ," 입니다.")
elif d == 0:
    print("실근은 -1 입니다.")
elif d < 0:
    print("이 방정식은 해가 존재하지 않습니다.")