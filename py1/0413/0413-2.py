import random
import time

count = 0
correctcount = 0

startTime = time.time()

while count < 5:
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)

    if n1 < n2:
        n1, n2 = n2, n1

    answer = eval(input("What is " + str(n1) + " - " + str(n2) + " ? "))

    if n1 - n2 == answer:
        print("You are correct")
        correctcount = correctcount + 1
    else:
        print("Nonono... answer is " , n1-n2)

    count = count + 1

endTime = time.time()
testTime = int(endTime - startTime)
print("correct count = " , correctcount, ", Time is" , testTime, "seconds")