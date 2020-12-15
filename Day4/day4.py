# Get data from input file
with open("day4_input.txt", "r") as inputFile:
    batch = inputFile.read()

# Trim input
batch = batch.split("\n\n")

for i in range(0, len(batch)):
    batch[i] = batch[i].replace(' ', '\n')
    batch[i] = batch[i].split('\n')

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID) (optional)
requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
#   If cm, the number must be at least 150 and at most 193.
#   If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
validEyeColor = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

result1 = 0
result2 = 0

for item in batch:
    tmpStr = ""
    for field in item:
        tmpStr = tmpStr + field[0:3] + " "
    
    if all(x in tmpStr for x in requiredFields):    
        result1 += 1
        
        field_check = 1
        for field in item:
            if field[0:3] == requiredFields[0]:     # byr (Birth Year) - four digits; at least 1920 and at most 2002.
                # Check if year is exactly 4 characters
                if len(field) == 8:
                    # Check if substring can be converted to integer
                    try:
                        byr = int(field[4:8])
                        # Check if year is within accepted range
                        if not (1920 <= byr <= 2002):
                            field_check = 0
                    except:
                        field_check = 0
                else:
                    field_check = 0
                
            elif field[0:3] == requiredFields[1]:   # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
                # Check if year is exactly 4 characters
                if len(field) == 8:
                    # Check if substring can be converted to integer
                    try:
                        byr = int(field[4:8])
                        # Check if year is within accepted range
                        if not (2010 <= byr <= 2020):
                            field_check = 0
                    except:
                        field_check = 0
                else:
                    field_check = 0

            elif field[0:3] == requiredFields[2]:   # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
                # Check if year is exactly 4 characters
                if len(field) == 8:
                    # Check if substring can be converted to integer
                    try:
                        byr = int(field[4:8])
                        # Check if year is within accepted range
                        if not (2020 <= byr <= 2030):
                            field_check = 0
                    except:
                        field_check = 0
                else:
                    field_check = 0

            elif field[0:3] == requiredFields[3]:   # hgt (Height) - a number followed by either cm or in:
                                                    #   If cm, the number must be at least 150 and at most 193.
                                                    #   If in, the number must be at least 59 and at most 76.
                # Check if string ends with "cm" or "in"
                tmpStr = field[len(field)-2:len(field)]
                if tmpStr == "cm" or tmpStr == "in":
                    # Check if substring can be converted to number
                    try:
                        hgt = float(field[4:len(field)-2])
                        # Check if height is within accepted range
                        if tmpStr == "cm":
                            if not (150 <= hgt <= 193):
                                field_check = 0
                        else:
                            if not (59 <= hgt <= 76):
                                field_check = 0
                    except:
                        field_check = 0
                else:
                    field_check = 0

            elif field[0:3] == requiredFields[4]:   # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
                # Check if hair color code has correct length
                hcl = field[4:len(field)]
                if len(hcl) == 7:
                    # Check if hair color code only contains valid characters
                    if hcl[0] == "#":
                        s = {'#', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a','b','c','d','e','f'}
                        if not s.issuperset(hcl):
                            field_check = 0
                    else:
                        field_check = 0
                else:
                    field_check = 0

            elif field[0:3] == requiredFields[5]:   # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
                # Check if eye color is valid
                tmpStr = field[4:len(field)]
                if not any(x in tmpStr for x in validEyeColor):
                    field_check = 0

            elif field[0:3] == requiredFields[6]:   # pid (Passport ID) - a nine-digit number, including leading zeroes.
                tmpStr = field[4:len(field)]
                if len(tmpStr) == 9:
                    try:
                        pid = int(tmpStr)
                    except:
                        field_check = 0
                else:
                    field_check = 0

        result2 += field_check

print(result1)
print(result2)
