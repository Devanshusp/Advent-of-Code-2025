import bisect

# read the input
# input_file = "D5_input_test.txt"
input_file = "D5_input.txt"

fresh_range: list[tuple] = []
given_ingredients: list[int] = []

with open(input_file) as file:
    for line in file:
        data = line.split("-")

        if len(data) == 2:
            # two numbers -> range of fresh ingredients
            num_a, num_b = data
            bisect.insort(fresh_range, (int(num_a), int(num_b)), key=lambda x: x[0])
        elif len(data) == 1 and data[0] != "\n":
            # one number -> ingredients
            given_ingredients.append(int(data[0]))


# combine ranges
def combine_overlapping_ranges(range_list: list[tuple]) -> list[tuple]:
    N = len(range_list)
    cleaned_range_list = []

    index = 0
    while index < N:
        num_a, num_b = range_list[index]
        while index + 1 < N and range_list[index + 1][0] <= num_b:
            num_b = max(num_b, range_list[index + 1][1])
            index += 1

        cleaned_range_list.append((num_a, num_b))
        index += 1

    return cleaned_range_list


fresh_range = combine_overlapping_ranges(fresh_range)
count_fresh_given = 0

# count of fresh ingredients from ones given
for ingredient in given_ingredients:
    index = bisect.bisect_left(fresh_range, ingredient, key=lambda x: x[0])

    # check behind
    if index - 1 >= 0 and fresh_range[index - 1][0] <= ingredient <= fresh_range[index - 1][1]:
        count_fresh_given += 1
        continue

    # check ahead
    if index < len(fresh_range) and fresh_range[index][0] <= ingredient <= fresh_range[index][1]:
        count_fresh_given += 1
        continue

# count of total fresh ingredients
count_fresh_all = 0
for lo_range, hi_range in fresh_range:
    count_fresh_all += hi_range - lo_range + 1


print("Problem 1", count_fresh_given)
print("Problem 2", count_fresh_all)
