
def execute(program):
    accumulator = 0
    progCnt = 0
    terminate = False
    infinite = False
    pcHistory = []

    # Clear line executed key
    for i in range(0, len(program)):
        program[i]['exec'] = 0

    while not terminate:
        line = program[progCnt]

        if progCnt == len(program) - 1:
            terminate = True

        if (line['exec'] != 0):
            terminate = True
            infinite = True
        else:
            program[progCnt]['exec'] += 1

            if line['cmd'] == 'nop':
                pcHistory.append(progCnt)
                progCnt += 1
            elif line['cmd'] == 'acc':
                accumulator += line['arg']
                progCnt += 1
            elif line['cmd'] == 'jmp':
                pcHistory.append(progCnt)
                progCnt += line['arg']

    return {'accum':accumulator, 'err':infinite, 'pcHist': pcHistory}

# Get data from input file
with open('day8_input.txt', 'r') as inputFile:
    scanInput = inputFile.read()

# Sort data
scanInput = scanInput.split('\n')
Program = []

for line in scanInput:
    Program.append({'cmd':line[0:3], 'arg':int(line[4:len(line)]), 'exec':0})

# Find accumulator value prior to first repeated command
result1 = execute(Program)
cntList = result1['pcHist']
result1 = result1['accum']
print(result1)

# Fix program and find accumulator value when program runs correctly
fixed = False
i = len(cntList)-1

while (not fixed) and (i >= 0):
    suspect = Program[cntList[i]]
    
    # Change command
    if suspect['cmd'] == 'nop':
        Program[cntList[i]]['cmd'] = 'jmp'
    elif suspect['cmd'] == 'jmp':
        Program[cntList[i]]['cmd'] = 'nop'
        
    result2 = execute(Program)

    if result2['err'] == False:
        fixed = True
    else:
        # Reverse change
        Program[cntList[i]]['cmd'] = suspect['cmd']

    i -= 1

result2 = result2['accum']
print(result2)
