secsPerYear = 365 * 24 * 60 * 60
birthsPerYear = secsPerYear // 7
deathsPerYear = secsPerYear // 13
immigrantsPerYear = secsPerYear // 45
currPopulation = 312032486 

for y in range(1, 6):
    yPopulation = currPopulation + birthsPerYear - deathsPerYear + immigrantsPerYear
    print(yPopulation)
    currPopulation = yPopulation