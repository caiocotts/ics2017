invest = float(input("Enter investment ammount: "))
annInterest = float(input("Enter annual interest rate: "))
numYears = int(input("Enter number of years: "))

monInterest = annInterest / 12
numOfMonths = numYears * 12

futureInvest = invest * (1 + monInterest/100) ** numOfMonths

print("Accumulate value is: %1.2f" % futureInvest)
