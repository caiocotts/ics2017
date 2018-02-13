### Question 8
width = 4.5
height = 7.9
area = width * height
perimeter = 2 * width + 2 * height
print("%.2f" % area)
print("%.2f" % perimeter)

### Question 9
kmPerhour = 14 * 60 / 45.5
mPerhour = kmPerhour / 1.6
print(mPerhour)

### Question 10
secsPerYear = 365 * 24 * 60 * 60
birthsPerYear = secsPerYear // 7
deathsPerYear = secsPerYear // 13
immigrantsPerYear = secsPerYear // 45
currPopulation = 312032486
for y in range(1, 6):
    yPopulation = currPopulation + birthsPerYear - deathsPerYear + immigrantsPerYear
    print(yPopulation)
    currPopulation = yPopulation
