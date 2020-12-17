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
                # Get visible seats
                visibleSeats = {}
                dist = 1
                while (dist < length) and (len(visibleSeats) < 8): 
                    Dir = {
                        'left': {'l': l, 'w': w-dist},
                        'right': {'l': l, 'w': w+dist},
                        'behind': {'l': l-dist, 'w': w},
                        'inFront': {'l':l+dist, 'w': w},
                        'behindLeft': {'l': l-dist, 'w': w-dist},
                        'behindRight': {'l': l-dist, 'w': w+dist},
                        'inFrontLeft': {'l': l+dist, 'w': w-dist},
                        'inFrontRight': {'l': l+dist, 'w': w+dist}
                    }

                    for key in Dir:
                        if (-1 < Dir[key]['l'] < length) and (-1 < Dir[key]['w'] < width):
                            if (prevSeatArea[Dir[key]['l']][Dir[key]['w']] != '.') and (key not in visibleSeats):
                                visibleSeats[key] = prevSeatArea[Dir[key]['l']][Dir[key]['w']]
                        else:
                            if key not in visibleSeats:
                                visibleSeats[key] = '.'

                    dist += 1
                    
                occupied = 0
                for key in visibleSeats:
                    if visibleSeats[key] == '#':
                        occupied += 1

                # Apply rules
                if prevSeatArea[l][w] == 'L' and occupied == 0:
                    seatArea[l][w] = '#'
                elif prevSeatArea[l][w] == '#' and occupied >= 5:
                    seatArea[l][w] = 'L'

# Count occupied seats
result2 = 0
for i in range(0, length):
    result2 += seatArea[i].count('#')

print(result2)
