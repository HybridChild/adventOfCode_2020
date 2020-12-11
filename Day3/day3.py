import math

# Get data from input file
inputFile = open("day3_input.txt", "r") 
forestMap = inputFile.read()
forestMap = forestMap.split('\n')

pos = 0
result1 = 0
result2 = 0

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
trees = []
for i in range(0, len(slopes)):
    trees.append(0)

slopeCnt = 0

for slope in slopes:
    pos = 0
    
    for i in range(0, len(forestMap)-1, slope[1]):
        if (forestMap[i][pos] == '#'):
            trees[slopeCnt] += 1

        pos += slope[0]
        if (pos >= len(forestMap[i])):
            pos -= len(forestMap[i])

    slopeCnt += 1
    
result1 = trees[1]
result2 = math.prod(trees)

print(result1)
print(result2)
