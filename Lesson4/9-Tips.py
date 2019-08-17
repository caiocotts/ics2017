subTotal = float(input("Enter the subtotal: "))
gratuityRate = int(input("Enter the gratuity rate: "))

tip = subTotal * gratuityRate / 100
total = subTotal + tip

print("The gratuity is %1.2f and the total is %1.2f" % (tip, total))
