def main():
    # input = open("Score.txt", "r") # 현재 디렉터리에 있을 경우

    oufile = open(r"C:\Users\User\PycharmProjects\Python\py1\0617\Score.txt", "w")  # "r" "w"

    # input = open("C:\\Users\\User\\PycharmProjects\\Python\\py1\\Score.txt", "r")

    oufile.write("Welcome to Python\n")
    oufile.write("HmmNya~~\n")

    oufile.close()

    infile = open("Presidents.txt", "r")
    print(" (1) Using read(): ")
    print(infile.read())
    infile.close()

    # Open file for input
    infile = open("Presidents.txt", "r")
    print("\n (2) Using read(number): ")
    s1 = infile.read(4) # 4개읽고
    print(s1)
    s2 = infile.read(10) # 10개 읽기
    print(repr(s2))
    infile.close()



main()
