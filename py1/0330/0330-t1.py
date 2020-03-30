Amount = eval(input("가격을 입력해주세용(123450 won): "))

remainingAmount = int(Amount)

# 5만원
오만원 = int(remainingAmount / 50000)
remainingAmount = int(remainingAmount % 50000)

# 만원
만원 = int(remainingAmount / 10000)
remainingAmount = (remainingAmount % 10000)

# 오천원
오천원 = int(remainingAmount / 5000)
remainingAmount = (remainingAmount % 5000)

# 천원
천원 = int(remainingAmount / 1000)
remainingAmount = (remainingAmount % 1000)

# 오백원
오백원 = int(remainingAmount / 500)
remainingAmount = (remainingAmount % 500)

# 백원
백원 = int(remainingAmount / 100)
remainingAmount = (remainingAmount % 100)

# 오십원
오십원 = int(remainingAmount / 50)
remainingAmount  = (remainingAmount % 50)

# 십원
십원 = int(remainingAmount / 10)

print("All money", Amount, "consists of\n",
      "\t", "5만원: ", 오만원, "\n",
      "\t", "1만원: ", 만원, "\n",
      "\t", "5천원: ", 오천원, "\n",
      "\t", "1천원: ", 천원, "\n",
      "\t", "5백원: ", 오백원, "\n",
      "\t", "1백원: ", 백원, "\n",
      "\t", "5십원: ", 오십원, "\n",
      "\t", "1십원: ", 십원, "\n")