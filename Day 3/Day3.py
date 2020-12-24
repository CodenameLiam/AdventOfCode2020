from functools import reduce

# Parse Input
f = open("Day 3/Input.txt", "r")
slope = f.read().split("\n")
edge = len(slope[0])

# Find the number of trees encountered for a given combination of right and down movements
def TreesEncountered(right, down) -> int:
    sledX, sledY, treesEncountered = 0, 0, 0

    # Loop until condition is met
    while True:
        sledX += right
        sledY += down

        # If we have reached the bottom of the slope, finish the loop
        if sledY >= len(slope):
            break
        
        # If we have reached the edge of the slope pattern, wrap around
        if sledX >= edge:
            sledX = sledX - edge
        
        # If the current coordinates are equal to a tree, add 1 to the tree encounter counter
        if slope[sledY][sledX] == "#":
            treesEncountered += 1

    return treesEncountered

# PART 1
print(f"Number of trees encountered in part 1: {TreesEncountered(3, 1)}\n")


# PART 2
slopeArray = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
encounteredArray = []

for values in slopeArray:
    treesEncountered = TreesEncountered(values[0], values[1])
    encounteredArray.append(treesEncountered)
    print(f"Number of trees encountered for {values}: {treesEncountered}")

print(f"Product of all trees encountered: {reduce((lambda x, y: x * y), encounteredArray)}")




