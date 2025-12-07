import math
from itertools import groupby

# read the input
# input_file = "D6_input_test.txt"
input_file = "D6_input.txt"

numbers_hor = []  # problem 1: read numbers horizontally
operations = []
raw_lines = []

with open(input_file) as file:
    for i, line in enumerate(file):
        raw_lines.append(line.rstrip("\n"))

        line = line.split()

        if not numbers_hor:
            numbers_hor = [[] for _ in range(len(line))]

        for j, num in enumerate(line):
            if num.isdigit():
                numbers_hor[j].append(int(num))

        # this will save the last line (operations) after loop is done
        operations = line


# prep for problem 2: normalize grid width and transpose
W = max(len(line) for line in raw_lines)
columns = list(zip(*[line.ljust(W) for line in raw_lines[:-1]]))

numbers_ver = []  # problem 2: read numbers vertically

# group columns by empty space vs content
for is_space, cols in groupby(columns, key=lambda c: all(x == " " for x in c)):
    if is_space:
        continue

    nums = []
    # read columns right -> left within the block
    for col in reversed(list(cols)):
        digits = "".join(x for x in col if x.isdigit())
        if digits:
            nums.append(int(digits))

    numbers_ver.append(nums)

total_hor = 0
total_ver = 0


for nums_h, nums_v, op in zip(numbers_hor, numbers_ver, operations):
    match op:
        case "*":
            total_hor += math.prod(nums_h)
            total_ver += math.prod(nums_v)
        case "+":
            total_hor += sum(nums_h)
            total_ver += sum(nums_v)

print("Problem 1", total_hor)
print("Problem 2", total_ver)
