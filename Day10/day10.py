with open('day10_input.txt', 'r') as inputFile:
    Adapters = inputFile.read()

Adapters = Adapters.split('\n')
for i in range(0, len(Adapters)):
    Adapters[i] = int(Adapters[i])

outlet = 0
myDevice = max(Adapters) + 3
Adapters.append(outlet)
Adapters.append(myDevice)
Adapters = sorted(Adapters)

ones = 0
threes = 0
conOnes = 0
arrangements = 1
Tribonacci = [1, 1, 2, 4, 7, 13, 24, 44, 81, 149]

for i in range(1, len(Adapters)):
    diff = Adapters[i] - Adapters[i-1]

    if diff == 1:
        ones += 1
        conOnes += 1
    elif diff == 3:
        threes += 1
        arrangements *= Tribonacci[conOnes]
        conOnes = 0

result1 = ones * threes
result2 = arrangements
print(result1)
print(result2)
