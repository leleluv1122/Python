import random

num = random.randint(1, 100)

print("Guess a number between 1 to 100")

guess = -1

while guess != num:
    guess = eval(input("Enter your guess: "))

    if guess == num:
        print("Correct number " , num)
    elif guess > num:
        print("Too high")
    else:
        print("Too low")