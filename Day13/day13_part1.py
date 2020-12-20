with open('day13_input.txt', 'r') as inputFile:
    busSchedule = inputFile.read()

busSchedule = busSchedule.split('\n')
earliestDeparture = int(busSchedule[0])
busSchedule = busSchedule[1]
busSchedule = busSchedule.replace('x,', '')
busSchedule = busSchedule.split(',')
earliestBus = 0

for i in range(0, len(busSchedule)):
    busSchedule[i] = {'ID': int(busSchedule[i])}
    
    departure = 0
    while departure < earliestDeparture:
        departure += busSchedule[i]['ID']

    busSchedule[i]['dep'] = departure
    busSchedule[i]['diff'] = departure - earliestDeparture

    if i == 0:
        earliest = busSchedule[i]['diff']
    elif busSchedule[i]['diff'] < earliest:
        earliest = busSchedule[i]['diff']
        earliestBus = i

result1 = busSchedule[earliestBus]['ID']*busSchedule[earliestBus]['diff']
print(result1)
