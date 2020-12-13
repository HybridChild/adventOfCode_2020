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
def recurse_bags (initial_bag, amount):
    bags_in_initial = RulesDict[initial_bag]

    if len(bags_in_initial) == 0:
        return amount

    cnt = 1

    for bag in bags_in_initial:
        cnt += recurse_bags(bag['bag_color'], bag['amount'])

    return cnt * amount

result2 = recurse_bags(myBagColor, 1) - 1 # Subtract your own bag
print(result2)
