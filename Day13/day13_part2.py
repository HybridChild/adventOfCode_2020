with open('day13_input.txt', 'r') as inputFile:
    busSchedule = inputFile.read()

busSchedule = busSchedule.split('\n')
busSchedule = busSchedule[1]
busSchedule = busSchedule.split(',')

busList = []
idxList = []
for i in range(0, len(busSchedule)):
    if busSchedule[i] != 'x':
        busList.append({'ID': int(busSchedule[i]),'nextDep': int(busSchedule[i]), 'matchStamp': [0, 0], 'mult': 1})
        if i != 0:
            idxList.append(i)
    else:
        busList.append('dummy')


stamp = 0
match = False
multiplier = 1
print(multiplier)

while not match:
    match = True
    for i in idxList:
        while busList[i]['nextDep'] < stamp:
            busList[i]['nextDep'] += busList[i]['ID']

        if (busList[i]['nextDep'] == stamp + i):
            if busList[i]['matchStamp'][1] == 0:
                if busList[i]['matchStamp'][0] == 0:
                    busList[i]['matchStamp'][0] = stamp
                else:
                    busList[i]['matchStamp'][1] = stamp
                    stampDiff = busList[i]['matchStamp'][1] - busList[i]['matchStamp'][0]
                    if multiplier < int(stampDiff / busList[0]['ID']):
                        multiplier = int(stampDiff / busList[0]['ID'])
                        busList[i]['mult'] = multiplier
                        print(busList[i])
        else:
            match = False
            break

    stamp += busList[0]['ID'] * multiplier

result2 = stamp - busList[0]['ID'] * multiplier
print(result2)
