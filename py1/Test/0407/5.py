# for, while

for i in range(3):
    print(i)
    print("철수: 안녕 영희야 뭐해?")
    print("영희: 안녕 철수야, 그냥 있어..")

############################################

i = 0

while(i < 3):
    print(i)
    print("철수: 안녕 영희야 뭐해?")
    print("영희: 안녕 철수야, 그냥 있어..")
    i = i + 1

############################################

i = 0
while True: # 무한루프
    print(i) # 0
    print("철수: 안녕 영희야 뭐해?")
    print("영희: 안녕 철수야, 그냥 있어..")
    i = i + 1

    if i > 2:
        break;

############################################

for i in range(100):
    print(i)
    print("철수: 안녕 영희야 뭐해?")
    print("영희: 안녕 철수야, 그냥 있어..")

    if i > 2:
        break

############################################

for i in range(3):
    print(i)
    print("철수: 안녕 영희야 뭐해?")
    print("영희: 안녕 철수야, 그냥 있어..")

    if i == 1:
        continue # 특이한 조건에서 이 조건을 실행시키고 싶지않음
    
    print("스니: 스니스니하뚜하뚜")