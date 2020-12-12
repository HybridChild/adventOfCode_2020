# Get data from input file
inputFile = open("day7_input.txt", "r")
scanInput = inputFile.read()
inputFile.close()

allRules = scanInput.split('\n')
Rules = []
bagsContainingMine = []

result1 = 0
result2 = 0

myBagColor = "shiny gold"
keyWord_Color = " bags contain "
keyWord_NoBags = "no other bags"

# Arrange rules in list
for rule in allRules:
    # Extract bag color
    try:
        idx = rule.index(keyWord_Color)
        thisBagColor = rule[0:idx]
        idx += len(keyWord_Color)
        rule = rule[idx:len(rule)]
    except:
        idx = -1
    
    # Identify what bags this one contains
    contains = []

    if keyWord_NoBags in rule:
        bagCount = 0
        bagColor = keyWord_NoBags
        contains.append([bagCount, bagColor])
    else:
        rule = rule.split(", ")
        
        for bag in rule:
            bagCount = int(bag[0])
            bagColor = bag[2:bag.index(" bag")]
            contains.append([bagCount, bagColor])

    Rules.append([thisBagColor, contains])


# Check which bags contain mine directly
for rule in Rules:
    for bag in rule[1]:
        if bag[1] == myBagColor:
            bagsContainingMine.append(rule[0])
            break


# Check which bags contain mine indirectly
containingBagsCount = len(bagsContainingMine)
checkCount = 0

while containingBagsCount != checkCount:
    checkCount = containingBagsCount
    bagsIndirectlyContainingMine = []
    for bag in bagsContainingMine:
        for rule in Rules:
            if not (rule[0] in bagsContainingMine) and not (rule[0] in bagsIndirectlyContainingMine):
                for bagColor in rule[1]:
                    if bagColor[1] == bag:
                        bagsIndirectlyContainingMine.append(rule[0])
                        break
                        
    bagsContainingMine += bagsIndirectlyContainingMine
    containingBagsCount = len(bagsContainingMine)

result1 = containingBagsCount

print(result1)
