import os.path
import random
import sys

def main():
    txt = input("파일 이름을 입력하세요: ")
    if os.path.isfile(txt):
        print("파일이 이미 존재합니다.")
        sys.exit()

    outfile = open(txt, "w")
    for i in range(50):
        outfile.write(str(random.randint(1, 50)) + " ")
    outfile.close()

    infile = open(txt, "r")
    s = infile.readline()
    print(s)

    infile.close()

main()