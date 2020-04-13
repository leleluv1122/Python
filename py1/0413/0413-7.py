# break : 완전히 loop에서 빠져나옴
# continue : 특정 iteration에서 나옴

sum = 0
number = 0

while number < 20:
    number += 1
    sum += number
    if sum >= 100:
        break # loop에서 완전히 빠져나옴

print("The number is ", number)
print("The sum is ", sum)
print()

sum = 0
number = 0

while number < 20:
    number += 1
    if number == 10 or number == 11:
        continue
    sum += number

print("The sum is ", sum)