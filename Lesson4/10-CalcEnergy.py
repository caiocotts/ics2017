waterWeigth = float(input("Enter the ammout of water in kilograms: "))
initialTemperature = float(input("Enter the initial temperature: "))
finalTemperature = float(input("Enter the final temperature: "))
energy =  waterWeigth * (finalTemperature - initialTemperature) * 4184

print("The energy needed is", energy)