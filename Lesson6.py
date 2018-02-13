ammount = float(input("Enter the amount of meal: "))
tipPercentage = float(input("Enter the tip as a percentage: "))
taxRate = float(input("Enter the tax rate as a percent: "))

tip = ammount * tipPercentage / 100
tax = ammount * taxRate / 100

print("\nAmount of meal   Tip     Tax     Total")
print("%-16.2f %-7.2f %-7.2f %-7.2f" % (ammount, tip, tax, ammount + tip + tax))