### Question 1
num = [127.899, 3465.148, 3.776, 264.821, 88.081, 799.999]
for i in range(0, len(num)):
    print(format(num[i], "7.2f"))


### Question 2
time = int(input("Enter a time less than 4.5 seconds: "))
height = 100 - 4.9 * time ** 2
print("The height of the object is:", height, "meters")


### Question 3
diameter = int(input("Enter the diameter of the pizza in inches: "))
labourCost = 0.75
rentCost = 1.00
materialsCost = 0.05 * diameter ** 2
cost = labourCost + rentCost + materialsCost
print("The cost of making the pizza is: $%0.2f" % cost)


### Question 4
mass = int(input("Enter the mass in kilograms: "))

c = 3 * 10**8
e = mass * c**2
print("The energy produced in Joules is:", format(e, "g"))

numberOfBulbs = e / 360000
print("The number of 100-watt light bulds powered =", format(numberOfBulbs, "g"))

