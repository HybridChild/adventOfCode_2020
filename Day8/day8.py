import copy

def execute(program):
    accumulator = 0
    progCnt = 0
    terminate = False
    infinite = False

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
                progCnt += 1
            elif line['cmd'] == 'acc':
                accumulator += line['arg']
                progCnt += 1
            elif line['cmd'] == 'jmp':
                progCnt += line['arg']

    return {'accum':accumulator, 'err':infinite}

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
result1 = result1['accum']
print(result1)

# Fix program and find accumulator value if program runs correctly
fixed = False
i = 0

while (not fixed) and (i < len(Program)):
    # Change line
    changed = False
    AlteredProgram = copy.deepcopy(Program)

    while (not changed) and (i < len(Program)):
        if AlteredProgram[i]['cmd'] == 'nop':
            AlteredProgram[i]['cmd'] = 'jmp'
            changed = True
        elif AlteredProgram[i]['cmd'] == 'jmp':
            AlteredProgram[i]['cmd'] = 'nop'
            changed = True
        
        i += 1

    result2 = execute(AlteredProgram)

    if result2['err'] == False:
        fixed = True

result2 = result2['accum']

print(result2)
