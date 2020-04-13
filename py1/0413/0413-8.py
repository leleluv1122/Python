import random
number = random.randint(1, 100)

print("Guess a magic number between 1 and 100")

while True:
    guess = eval(input("Enter your guess: "))

    if guess == number:
        print("Yes, the number is ", number)
        break
    elif guess > number:
        print("Too high")
    else:
        print("Too low")