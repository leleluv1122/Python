human = 312032486

d = 365 * 24 * 60 * 60 * 5

human += d//7
human -= d//13
human += d//45

print(human)