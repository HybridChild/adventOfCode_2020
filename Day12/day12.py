def navigateShip(Instructions):
    # Latitude = North(+) - South(-)
    # Longitude = East(+) - West(-)

    Position = {'latitude': 0, 'longitude': 0}
    Compas = ['N', 'E', 'S', 'W']
    facing = 1

    for inst in Instructions:
        if inst['dir'] == 'F':
            if Compas[facing] == 'N':
                Position['latitude'] += inst['val']
            elif Compas[facing] == 'S':
                Position['latitude'] -= inst['val']
            elif Compas[facing] == 'E':
                Position['longitude'] += inst['val']
            elif Compas[facing] == 'W':
                Position['longitude'] -= inst['val']
        
        elif inst['dir'] == 'N':
            Position['latitude'] += inst['val']
        elif inst['dir'] == 'S':
            Position['latitude'] -= inst['val']
        elif inst['dir'] == 'E':
            Position['longitude'] += inst['val']
        elif inst['dir'] == 'W':
            Position['longitude'] -= inst['val']

        elif inst['dir'] == 'R':
            facing += int(inst['val']/90)
            while facing >= len(Compas):
                facing -= len(Compas)

        elif inst['dir'] == 'L':
            facing -= int(inst['val']/90)
            while facing < 0:
                facing += len(Compas)

    Manhattan_distance = abs(Position['latitude']) + abs(Position['longitude'])
    return Manhattan_distance


def navigateWayPoint(Instructions):
    # Latitude = North(+) - South(-)
    # Longitude = East(+) - West(-)

    shipPosition = {'latitude': 0, 'longitude': 0}
    wayPointPosition = {'latitude': 1, 'longitude': 10}  # Position relative to ship

    for inst in Instructions:
        if inst['dir'] == 'F':
            shipPosition['latitude'] += (wayPointPosition['latitude'] * inst['val'])
            shipPosition['longitude'] += (wayPointPosition['longitude'] * inst['val'])
        
        elif inst['dir'] == 'N':
            wayPointPosition['latitude'] += inst['val']
        elif inst['dir'] == 'S':
            wayPointPosition['latitude'] -= inst['val']
        elif inst['dir'] == 'E':
            wayPointPosition['longitude'] += inst['val']
        elif inst['dir'] == 'W':
            wayPointPosition['longitude'] -= inst['val']

        elif inst['dir'] == 'R':
            turns = int((inst['val']/90) % 4)
            newPos = {}
            if turns == 1:
                newPos = {'latitude': -wayPointPosition['longitude'], 'longitude': wayPointPosition['latitude']}
            elif turns == 2:
                newPos = {'latitude': -wayPointPosition['latitude'], 'longitude': -wayPointPosition['longitude']}
            elif turns == 3:
                newPos = {'latitude': wayPointPosition['longitude'], 'longitude': -wayPointPosition['latitude']}

            wayPointPosition = newPos

        elif inst['dir'] == 'L':
            turns = int((inst['val']/90) % 4)
            newPos = {}
            if turns == 1:
                newPos = {'latitude': wayPointPosition['longitude'], 'longitude': -wayPointPosition['latitude']}
            elif turns == 2:
                newPos = {'latitude': -wayPointPosition['latitude'], 'longitude': -wayPointPosition['longitude']}
            elif turns == 3:
                newPos = {'latitude': -wayPointPosition['longitude'], 'longitude': wayPointPosition['latitude']}

            wayPointPosition = newPos

    Manhattan_distance = abs(shipPosition['latitude']) + abs(shipPosition['longitude'])
    return Manhattan_distance
            


with open('day12_input.txt', 'r') as inputFile:
    Instructions = inputFile.read()

Instructions = Instructions.split('\n')
for i in range(0, len(Instructions)):
    inst = Instructions[i]
    direc = inst[0]
    val = int(inst[1:len(inst)])
    Instructions[i] = {'dir': direc, 'val': val}

result1 = navigateShip(Instructions)
print(result1)

result2 = navigateWayPoint(Instructions)
print(result2)
