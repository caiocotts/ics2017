### Minds On
miles = 100
kilometers = miles * 1.61
print(kilometers)

### Question 1
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
print("The average of", num1, num2, num3, "is", (num1 + num2 + num3) / 3)

### Question 2
tempC = int(input("Enter the temperature in Celsius scale: "))
tempF = 9/5 * tempC + 32
print(tempC, "degrees Celsius =", tempF, "degrees Fahrenheit")

### Question 3
length = int(input("Enter length: "))
width = int(input("Enter width: "))
perimeter = length * 2 + width * 2
area = width * length
print("The area is: %1.0f" % area)
print("The perimeter is: %1.0f" % perimeter)

### Question 4
print ("a    b    a ** b")
for a in range(1, 6):
    b = a + 1
    print("%-4d %-4d %d" % (a, b, a ** b))
    
### Question 5
import math
sL = float(input("Enter the side length: "))
area = (3 * math.sqrt(3) / 2) * sL**2
print("The area of the hexagon is", area)

#### Question 6
invest = float(input("Enter investment ammount: "))
annInterest = float(input("Enter annual interest rate: "))
numYears = int(input("Enter number of years: "))

monInterest = annInterest / 12
numOfMonths = numYears * 12

futureInvest = invest * (1 + monInterest/100) ** numOfMonths

print("Accumulate value is: %1.2f" % futureInvest)

