d = {}

a = ""

while a != 'q':
    a = input("\'a\' to add word, \'l\' to lookup table, \'q\' to quit: ")
    if a == 'q':
        break
    elif a == 'a':
        word = input("Type the word: ")
        definition = input("Type the definition: ")

        d[word] = definition

    elif a == 'l':
        word = input("Type the word: ")
        b = False
        for key, value in d.items():
            if key == word:
                b = True
                w = value
        if b == True:
            print(w)
        elif b == False:
            print("The word is not in the dictionary")