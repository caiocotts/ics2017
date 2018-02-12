
print("----------------------------")

nameItem1 = str(input("Input name of item 1:"))
numItem1 = int(input("Input quantity of item 1:"))
priceItem1 = float(input("Input price of item 1:"))

print("----------------------------")

nameItem2 = str(input("Input name of item 2:"))
numItem2 = int(input("Input quantity of item 2:"))
priceItem2 = float(input("Input price of item 2:"))

print("----------------------------")

nameItem3 = str(input("Input name of item 3:"))
numItem3 = int(input("Input quantity of item 3:"))
priceItem3 = float(input("Input price of item 3:"))

print("\nYour bill:")
print("-------------------------------------------------------")

total1 = priceItem1 * numItem1
total2 = priceItem2 * numItem2
total3 = priceItem3 * numItem3

print("Item                  Quantity      Price      Total")
print("%-18s %4d %16.2f %10.2f" % (nameItem1, numItem1, priceItem1, total1))
print("%-18s %4d %16.2f %10.2f" % (nameItem2, numItem2, priceItem2, total2))
print("%-18s %4d %16.2f %10.2f" % (nameItem3, numItem3, priceItem3, total3))

subTotal = total1 + total2 + total3
tax = subTotal * 6.25 / 100
total = subTotal + tax

print("-------------------------------------------------------")
print("Subtotal %43.2f" % (subTotal))
print("6.25%% sales tax %35.2f" % (tax))
print("Total %46.2f" % (total))
