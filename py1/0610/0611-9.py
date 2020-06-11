def main():
    filename = input("Enter a filename: ").strip()
    infile = open(filename, "r")

    wordCounts = {}
    for line in infile:
        processLine(line.lower(), wordCounts)

    pairs = list(wordCounts.items())

    items = [[count, word] for (word, count) in pairs]
    items.sort(reverse = True)

    for count, word in items[ : 10]:
        print(word, count, sep = '\t')


def processLine(line, wordCounts):
    line = replacePunctuation(line)
    words = line.split()
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1


def replacePunctuation(line):
    for oh in line:
        if oh in "~@#$%^&*()_+=-<>?/,.;:!{}[]|'\"":
            line = line.replace(oh, " ")

    return line

main()