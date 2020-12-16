import copy

with open('day11_input.txt', 'r') as inputFile:
    seatArea = inputFile.read()

seatArea = seatArea.split('\n')
length = len(seatArea)
width = len(seatArea[0])

for i in range(0, length):
    seatArea[i] = list(seatArea[i])


# Rules
# - If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# - If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# - Otherwise, the seat's state does not change.

prevSeatArea = []
while prevSeatArea != seatArea:
    prevSeatArea = copy.deepcopy(seatArea)

    for l in range(0, length):
        for w in range(0, width):
            # If not floor
            if prevSeatArea[l][w] != '.':
                # Get immediate seats
                immediateSeats = []
                for ll in range(l-1, l+2):
                    for ww in range(w-1, w+2):
                        # If seat is not itself
                        if ll != l or ww != w:
                            # If seat is inside area
                            if (-1 < ll < length) and (-1 < ww < width):
                                immediateSeats.append(prevSeatArea[ll][ww])
                
                # Apply rules
                if prevSeatArea[l][w] == 'L' and '#' not in immediateSeats:
                    seatArea[l][w] = '#'
                elif prevSeatArea[l][w] == '#' and immediateSeats.count('#') >= 4:
                    seatArea[l][w] = 'L'

# Count occupied seats
result1 = 0
for i in range(0, length):
    result1 += seatArea[i].count('#')

print(result1)
