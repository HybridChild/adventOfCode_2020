# Get data from input file
inputFile = open("day7_input.txt", "r")
scanInput = inputFile.read()
inputFile.close()

allRules = scanInput.split('\n')
RulesDict = {}

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

    if not (keyWord_NoBags in rule):
        rule = rule.split(", ")
        
        for bag in rule:
            bagCount = int(bag[0])
            bagColor = bag[2:bag.index(" bag")]
            contains.append({'amount': bagCount, 'bag_color': bagColor})

    # Add to dictionary
    RulesDict[thisBagColor] = contains

# Find how many bags mine contains
def recurse_bags (initial_bag):
    bags_in_initial = RulesDict[initial_bag]

    if len(bags_in_initial) == 0:
        return 0

    cnt = 0

    for bag in bags_in_initial:
        tmp = recurse_bags(bag['bag_color'])

        if (tmp == 0):
            cnt += bag['amount']
        else:
            cnt += tmp * bag['amount']

    return cnt

result2 = recurse_bags(myBagColor)
print(result2)
