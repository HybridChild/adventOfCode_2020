length_preamble = 25

def isSumOfTwo(arr, sum):
    arr = sorted(arr)
    l = 0
    r = len(arr) - 1

    while l < r:
        if (arr[l] + arr[r]) == sum:
            return True
        elif (arr[l] + arr[r]) < sum:
            l += 1
        else:   # arr[l] + arr[r] > sum
            r -= 1

    return False


with open('day9_input.txt', 'r') as inputFile:
    scanInput = inputFile.read()

scanInput = scanInput.split('\n')
for i in range(0, len(scanInput)):
    scanInput[i] = int(scanInput[i])

i = length_preamble

while i < len(scanInput):
    newNum = scanInput[i]
    preamble = scanInput[i-length_preamble: i]
    
    if not isSumOfTwo(preamble, newNum):
        result1 = newNum

        i = len(scanInput) # break while loop
    
    i += 1

print(result1)

winSize = 2
while winSize < len(scanInput):
    i = winSize

    while i < len(scanInput):
        contiguous = scanInput[i-winSize: winSize]

        if sum(contiguous) == result1:
            result2 = max(contiguous) + min(contiguous)
            
            # Break while loops
            winSize = len(scanInput)
            i = len(scanInput)
        
        i += 1
    
    winSize += 1

print(result2)
