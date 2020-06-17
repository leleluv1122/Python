import os.path
if os.path.isfile("Score.txt"):
    print("Score.txt exists")

def main():
    #Open file for input
    infile = open("Presidents.txt", "r")
    print("\n (3) Using readline(): ")
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()

    print(repr(line1))
    print(repr(line2))
    print(repr(line3))
    print(repr(line4))

    infile.close()

main()