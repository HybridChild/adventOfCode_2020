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
Differences = []

for i in range(1, len(Adapters)):
    diff = Adapters[i] - Adapters[i-1]
    Differences.append(diff)

    if diff == 1:
        ones += 1
    elif diff == 3:
        threes += 1

result1 = ones * threes
print(result1)
