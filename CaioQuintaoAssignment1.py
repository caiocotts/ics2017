#####################################################################################
# Question 1 - ChangeCalculator
#
# DONE IN CLASS

#####################################################################################
# Question 2 - CashRegister

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
print("-----------------------------------------------------")

total1 = priceItem1 * numItem1
total2 = priceItem2 * numItem2
total3 = priceItem3 * numItem3

print("Item                  Quantity    Price      Total")
print("%-21s %-11d %-10.2f %-10.2f" % (nameItem1, numItem1, priceItem1, total1))
print("%-21s %-11d %-10.2f %-10.2f" % (nameItem2, numItem2, priceItem2, total2))
print("%-21s %-11d %-10.2f %-10.2f" % (nameItem3, numItem3, priceItem3, total3))

subTotal = total1 + total2 + total3
tax = subTotal * 6.25 / 100
total = subTotal + tax

print("-----------------------------------------------------")
print("Subtotal %41.2f" % (subTotal))
print("6.25%% sales tax %34.2f" % (tax))
print("Total %44.2f" % (total))


#####################################################################################
# Question 3 - Calculating Grade

nameExercise1 = input("Name of exercise 1: ")
score1 = int(input("Score received for exercise 1: "))
totalPointsPossible1 = int(input("Total points possible for exercise 1: "))
nameExercise2 = input("Name of exercise 2: ")
score2 = int(input("Score received for exercise 2: "))
totalPointsPossible2 = int(input("Total points possible for exercise 2: "))
nameExercise3 = input("Name of exercise 3: ")
score3 = int(input("Score received for exercise 3: "))
totalPointsPossible3 = int(input("Total points possible for exercise 3: "))

totalScore = score1 + score2 + score3
totalPointsPossible = totalPointsPossible1 + totalPointsPossible2 + totalPointsPossible3

totalGrade = totalScore / totalPointsPossible * 100

print("\nExercise        Score      Total Possible")
print("%-15s %-10d %-10d" % (nameExercise1, score1, totalPointsPossible1))
print("%-15s %-10d %-10d" % (nameExercise2, score2, totalPointsPossible2))
print("%-15s %-10d %-10d" % (nameExercise3, score3, totalPointsPossible3))
print("Total           %-10d %-10d" % (totalScore, totalPointsPossible))
print("Your total is %d out of %d, or %0.2f%%" % (totalScore, totalPointsPossible, totalGrade))


#####################################################################################
# Question 4 - Weighted Average

print("Please enter your test grades: ")
test1 = int(input("Test 1: "))
test2 = int(input("Test 2: "))
print("\nPlease enter your quiz grades: ")
quiz1 = int(input("Quiz 1: "))
quiz2 = int(input("Quiz 2: "))
quiz3 = int(input("Quiz 3: "))
print("\nPlease enter your homework average: ")
homeworkAverage = float(input("Homework: "))

testAverage = (test1 + test2) / 2
quizAverage = ((quiz1 + quiz2 + quiz3) / 3)

finalGrade = (testAverage * 50 / 100) + (quizAverage * 30 / 100) + (homeworkAverage * 20 / 100)
print("\nTest Average:", format(testAverage, "0.2f"))
print("Quiz Average:", format(quizAverage, "0.2f"))
print("Final Grade:", format(finalGrade, "0.2f"))