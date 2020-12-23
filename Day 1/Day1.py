import itertools
import numpy
import time

# Parse Input
f = open("Day 1/Input.txt", "r")
stringInput = (f.read().split("\n")) 
input = list(map(lambda s: int(s), stringInput))

def solutionBrute(iterations):
    # For every combination of numbers, find where the two 
    # equal 2020 and then multiply them together. Print
    # the result
    tic = time.perf_counter()
    for numbers in itertools.combinations(input, iterations): 
        if sum(numbers) == 2020:
            toc = time.perf_counter()
            # The two numbers
            print(f"Numbers: {numbers}")

            # Confirmation
            print(f"The sum of these numbers is: {sum(numbers)}")

            # Their Index
            print(f"Index: {[input.index(number) for number in numbers]}")

            # Answer
            print(f"Answer {numpy.prod(numbers)}") 

            print(f"It took {toc - tic:0.6f} seconds to find this solution")

# PART 1
print("\nSolution to Part 1:")
solutionBrute(2)

# PART 2
print("\nSolution to Part 2:")
solutionBrute(3)


# Faster solution to part 1
def solution():
    target = 2020
    halfTarget = 2020//2

    tic = time.perf_counter()

    # Find values of x such that 2020 - x is also in the list
    validSets = {target-x for x in input if x<=halfTarget} & {x for x in input if x>halfTarget}
    pairs = {(target-x, x) for x in validSets}

    toc = time.perf_counter()

    print(f"Numbers using faster solution: {pairs}")

    print(f"It took {toc - tic:0.6f} seconds to find this solution")


print("\nSolution to Part 1 Using Set Logic:")
solution()