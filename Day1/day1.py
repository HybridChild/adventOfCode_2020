# Get data from input file
inputFile = open("day1_input.txt", "r") 
input = inputFile.read()
inputFile.close()
input = input.split()

# use list comprehension to convert to integers 
input = [int(i) for i in input]

result1 = 0
result2 = 0

for i in range(0, len(input)):
    for j in range(i+1, len(input)):
        if (input[i]+input[j]) == 2020:
                result1 = input[i]*input[j]

        for k in range(j+1, len(input)):
            if (input[i]+input[j]+input[k]) == 2020:
                result2 = input[i]*input[j]*input[k]

print(result1)
print(result2)