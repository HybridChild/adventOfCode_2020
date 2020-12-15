# Get data from input file
inputFile = open("day2_input.txt", "r")

result1 = 0
result2 = 0

for line in inputFile:
    items = line.split(' ')
    items[0] = items[0].split('-')
    items[0] = [int(i) for i in items[0]]
    items[1] = items[1].replace(':', '')

    # Analyse 1
    if (items[2].count(items[1]) >= items[0][0] and items[2].count(items[1]) <= items[0][1]):
        result1 += 1
    
    # Analyse 2
    idx1 = items[0][0] - 1
    idx2 = items[0][1] - 1

    if (items[2][idx1] == items[1] or items[2][idx2] == items[1]):
        if not (items[2][idx1] == items[1] and items[2][idx2] == items[1]):
            result2 += 1

inputFile.close()

print(result1)
print(result2)
