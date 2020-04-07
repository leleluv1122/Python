def chat(name1, name2, age):
    print("%s: 안녕? 넌 몇 살이니?" % name1)
    print("%s: 나? 나는 %d" % (name2, age))

chat("승희", "호준", 24)
chat("철수", "영희", 20)

def dsum(a, b):
    result = a + b
    return result

d = dsum(150, 370)
print(d)