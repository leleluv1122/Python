s = "Welcome"
for ch in s:
    print(ch)

s = "Welcome"
for i in range(0, len(s), 2): # 2++
    print(s[i])

s = "welcome to python"
print(s.isalnum()) # 알파벳만 있고 르메릭?이없...
print("Welcome".isalpha()) # 알파가 잇다
print("2012".isdigit()) # digit이냐..? true
print("first Number".isidentifier()) # 식별자가 아니다...

print(s.endswith("thon"))
print(s.startswith("good"))
print(s.find("come"))
print(s.find("become"))
print(s.find("o"))
print(s.rfind("o"))
print(s.count("o"))

print(s.capitalize())
print(s.title())
print(s.lower())
print(s.upper())
print(s.swapcase())