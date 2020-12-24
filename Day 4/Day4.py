import re

# Parse input
f = open("Day 4/Input.txt", "r")
passportsRaw = f.read().split("\n\n")

# Declare arrays for storing valid passports
passportsValidP1 = []
passportsValidP2 = []

# Declare constansts
expectedFields = ["byr", "iyr", "eyr", 'hgt', 'hcl', 'ecl', 'pid' ]
eyeColour = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

# ----------------------------------------------------------------------------------------------- #
# Part 1
# ----------------------------------------------------------------------------------------------- #

# For each password, they will be valid if every expected field is found in the initial raw string
for passport in passportsRaw:
    isValid = all(list(map(lambda field: field in passport, expectedFields)))
    if isValid:
        passportsValidP1.append(passport)

# Print the answer
print(f"Number of valid passports in part 1: {len(passportsValidP1)}")

# ----------------------------------------------------------------------------------------------- #
# Part 2
# ----------------------------------------------------------------------------------------------- #

# Find a value for a given field from the list of values
def findValue(field, values):
    fieldValue = [value for value in values if field in value]

    if(fieldValue):
        return fieldValue[0].split(":")[1] 
    else:
        return False

# Validate a passport
def validateDict(passportDict):
    passportValidateDict = {
        "byr": validateYear(passportDict["byr"], 1920, 2002) if passportDict["byr"] != False else False,
        "iyr": validateYear(passportDict["iyr"], 2010, 2020) if passportDict["iyr"] != False else False,
        "eyr": validateYear(passportDict["eyr"], 2020, 2030) if passportDict["iyr"] != False else False,
        "hgt": validateHeight(passportDict["hgt"] if passportDict["hgt"] != False else False),
        "hcl": validateHair(passportDict["hcl"] if passportDict["hcl"] != False else False),
        "ecl": validateEyes(passportDict["ecl"] if passportDict["ecl"] != False else False),
        "pid": validateID(passportDict["pid"] if passportDict["pid"] != False else False),
    }

    return passportValidateDict

# Validates the year by ensuring the year argument is between the start and end date (could add type try/except blocks)
def validateYear(year, start, end):
    if(start <= int(year) <= end):
       return True
    else:
        return False

# Validates the height by checking units and ensuring the value falls within the specified limits
def validateHeight(height):
    # Type/array try/except block
    try:
        # Strip units to compare raw values
        heightNumeric = int(height[0:len(height)-2])
        if "cm" in height:
            return True if 150 <= heightNumeric <= 193 else False
        elif "in" in height:
            return True if 59 <= heightNumeric <= 76 else False
        else:
            return False
    except:
        return False

# Validates the hair colour by checking length, first char and subsequent 6 chars to ensure hex code
def validateHair(hair):
    try:
        if(len(hair) == 7):
            if hair[0] == "#" and re.match(r'^[0-9a-f]{6}$', hair[1:7] ):
                return True
            else:
                return False
        else:
            return False
    except:
        return False
    

# Validates eye colour by ensuring the value appears in the list of allowed eye colours
def validateEyes(eyes):
    return eyes in eyeColour

# Validates the id by ensuring it is 9 digits long and numeric
def validateID(id):
    try:
        return len(id) == 9 and id.isnumeric()
    except:
        return False
    

# For each password, split the passport into values, assign each value to a dictionary and then validate each key-value pair
for passport in passportsRaw:
    values = passport.split()

    passportDict = {
        "byr": findValue("byr", values),
        "iyr": findValue("iyr", values),
        "eyr": findValue("eyr", values),
        "hgt": findValue("hgt", values),
        "hcl": findValue("hcl", values),
        "ecl": findValue("ecl", values),
        "pid": findValue("pid", values),
    }

    # If all dictionary values are true, then the passport is valid
    isValid = all(value == True for value in validateDict(passportDict).values())

    if isValid:
        passportsValidP2.append(passportDict)

# Print the answer
print(f"Number of valid passports in part 2: {len(passportsValidP2)}")

    
    
