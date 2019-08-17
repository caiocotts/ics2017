### Question 7
feet =  float(input("Enter the value for feet: "))
meters = feet * 0.305
print("%1.1f feet is %1.4f meters" % (feet, meters))             

### Question 8
pounds =  float(input("Enter the value in pounds: "))
kilos = pounds * 0.454
print(pounds, "pounds is", kilos, "kilograms")

### Question 9
subTotal = float(input("Enter the subtotal: "))
gratuityRate = int(input("Enter the gratuity rate: "))

tip = subTotal * gratuityRate / 100
total = subTotal + tip

print("The gratuity is %1.2f and the total is %1.2f" % (tip, total))

### Question 10
waterWeigth = float(input("Enter the ammout of water in kilograms: "))
initialTemperature = float(input("Enter the initial temperature: "))
finalTemperature = float(input("Enter the final temperature: "))
energy =  waterWeigth * (finalTemperature - initialTemperature) * 4184

print("The energy needed is", energy)