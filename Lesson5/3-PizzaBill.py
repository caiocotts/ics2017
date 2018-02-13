diameter = int(input("Enter the diameter of the pizza in inches: "))
labourCost = 0.75
rentCost = 1.00
materialsCost = 0.05 * diameter ** 2
cost = labourCost + rentCost + materialsCost

print("The cost of making the pizza is: $%0.2f" % cost)
