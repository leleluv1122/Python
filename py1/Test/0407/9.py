fruit = ["사과", "사과", "바나나", "바나나", "딸기", "키위", "복숭아", "복숭아", "복숭아"]

d = {}
# d = {"사과": 2, "바나나": 2 ...}

for f in fruit:
    # f = "사과"  > f = "바나나"

    if f in d: # 사과 라는 key가 d라는 dictionary에 들어있어?
        d[f] = d[f] + 1 # "사과" 갯수 + 1
    else:
        d[f] = 1 # 만약 "사과"가 없으면, 그걸 dictionary에 넣고 value는 1

print(d)