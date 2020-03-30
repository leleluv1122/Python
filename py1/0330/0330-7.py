# Receive the amount
amount = eval(input("Enter an amount in double, e.g., 11.56: "))

# Convert the amount to cents 소수점 둘째짜리까지라서 100곱함
remainingAmount = int(amount * 100)

# Find the number of one dollars 소숫점을 없애기 위해...
numberOfDollars = int(remainingAmount / 100)
remainingAmount = int(remainingAmount % 100) # 나머지

# Find the number of quarters in the remaining amount 나머지중에 쿼터값
numberOfQuarters = int(remainingAmount / 25)
remainingAmount = remainingAmount % 25

# Find the number of dimes in the remaining amount 10센트
numberOfDimes = int(remainingAmount / 10)
remainingAmount = remainingAmount % 10

# Find the number of nickels in the remaining amount 5센트
numberOfNickels = int(remainingAmount / 5)
remainingAmount = remainingAmount % 5

# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount

# Display results
print("Your amount", amount, "consists of\n",
      "\t", numberOfDollars, "dollars\n",
      "\t", numberOfQuarters, "quarters\n",
      "\t", numberOfDimes, "dimes\n",
      "\t", numberOfNickels, "nickels\n",
      "\t", numberOfPennies, "pennies")