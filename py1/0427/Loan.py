class Loan:
    def __init__(self):
        self.annualInterestRate = 2.5
        self.numberOfYear = 1
        self.loanAmount = 1000
        self.borrower = "default"

    def getannualInterestRate(self):
        return self.annualInterestRate

    def setannualInterestRate(self, annu):
        self.annualInterestRate = annu

    def getYear(self):
        return self.numberOfYear

    def setYear(self, y):
        self.numberOfYear = y;

    def getAmount(self):
        return self.loanAmount

    def setAmount(self, m):
        self.loanAmount = m

    def getBorrower(self):
        return self.borrower

    def setBorrower(self, b):
        self.borrower = b

