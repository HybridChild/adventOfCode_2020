from string import ascii_lowercase

# Get data from input file
inputFile = open("day6_input.txt", "r")
scanInput = inputFile.read()
inputFile.close()

groupAnswers = scanInput.split("\n\n")

result1 = 0
result2 = 0

yesAnswersAny = []
yesAnswersEvery = []

i = 0
for group in groupAnswers:
    # Count how many questions anyone answered yes to
    yes = 0
    for c in ascii_lowercase:
        if c in group:
            yes += 1

    yesAnswersAny.append(yes)

    # split groups into individuals
    groupAnswers[i] = group.split('\n')
    i += 1

result1 = sum(yesAnswersAny)

# Count how many questions everyone answered yes to
for group in groupAnswers:
    yes = 0
    for c in ascii_lowercase:
        check = 1
        for person in group:
            if not (c in person):
                check = 0
        
        yes += check

    yesAnswersEvery.append(yes)

result2 = sum(yesAnswersEvery)

print(result1)
print(result2)
