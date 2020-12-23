# Parse Input
def parseLine(line):
    items = line.split()
    minMax = items[0].split("-")
    value = {
        "min": int(minMax[0]),
        "max": int(minMax[1]), 
        "char": items[1][0],
        "password": items[2],
    }
    return value

f = open("Day 2/Input.txt", "r")
stringInput = (f.read().split("\n")) 
values = list(map(parseLine, stringInput))


# Check if the line is valid (Part 1)
def isValid1(value):
    occurences = value["password"].count(value["char"])
    if value["min"] <= occurences <= value['max']:
        return True

def isEqual(password, value, character):
    try:
        if(password[value] == character):
            return True
    except IndexError as e:
        print(e)
        return False

# Check if the line is valid (Part 2)
def isValid2(value):
    equalMatches = 0
    if isEqual(value["password"], value["min"] - 1, value["char"]):
        equalMatches += 1
    if isEqual(value["password"], value["max"] - 1, value["char"]):
        equalMatches += 1

    if equalMatches == 1:
        return True
    else:
        return False 
    
    
# Part 1
print(f"The answer to part 1 is: {len([x for x in values if isValid1(x)])}")

# Part 2
print(f"The answer to part 2 is: {len([x for x in values if isValid2(x)])}")
