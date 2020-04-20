import RandomCharater

NUMBER_OF_CHARS = 175
CEARS_PER_LINE = 25

for i in range(NUMBER_OF_CHARS):
    print(RandomCharater.getRandomLowerCaseLetter(), end="")
    if(i+1)%CEARS_PER_LINE == 0:
        print() # Jump