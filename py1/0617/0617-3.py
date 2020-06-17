def main():
    infile = open("Presidents.txt", "r")
    print("\n (4) Using readlines(): ")
    print(infile.readlines())
    infile.close()

main()