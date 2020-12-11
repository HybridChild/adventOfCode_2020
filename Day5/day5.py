# Get data from input file
inputFile = open("day5_input.txt", "r")
scanInput = inputFile.read()
inputFile.close()

scanInput = scanInput.split('\n')

boardingPasses = []
IDs = []

result1 = 0
result2 = 0

for boardingPass in scanInput:
    row = 0
    column = 0
    ID = 0

    # Find row
    for i in range(0,7):
        if (boardingPass[i] == 'B'):
            row += (1 << 6-i)

    # Find Column
    ran = list(range(len(boardingPass)-3,len(boardingPass)))
    for i in ran:
        if boardingPass[i] == 'R':
            column += (1 << 9-i)

    # Calculate ID
    ID = (row * 8) + column

    if ID > result1:
        result1 = ID

    boardingPasses.append([row, column, ID])
    IDs.append(ID)

sortedIDs = sorted(IDs)
i = 1
while (sortedIDs[i] == sortedIDs[i+1]-1):
    i += 1

result2 = sortedIDs[i]+1

print(result1)
print(result2)
