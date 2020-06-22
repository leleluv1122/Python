def count(s, ch):
    cnt = 0
    for i in range(len(s)):
        if s[i] == ch:
            cnt+=1
    return cnt

def main():
    print(count("Welcome", 'e'))

main()