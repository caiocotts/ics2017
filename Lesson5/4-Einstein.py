mass = int(input("Enter the mass in kilograms: "))

c = 3 * 10**8
e = mass * c**2
print("The energy produced in Joules is:", format(e, "g"))

n = e / 360000
print("The number of 100-watt light bulds powered =", format(n, "g"))
