# read input
# input_file = "D2_input_test.txt"
input_file = "D2_input.txt"

id_ranges = []

with open(input_file) as file:
    file_str = file.read()
    for id_range in file_str.split(","):
        num_a, num_b = id_range.split("-")
        id_ranges.append((int(num_a), int(num_b)))


def sum_invalid_ids(min_val: int, max_val: int, count_rep: int, seen: set) -> int:
    max_val_len = len(str(max_val))

    # this is how long the repeating piece will be
    part_len = (max_val_len + 1) // count_rep

    if part_len > max_val_len or part_len == 0:
        # if the repeating part len is impossible, return 0
        return 0

    # make the repeating part of number
    part_int = int("9" * part_len)

    # use the repeating part to create the full number
    full_int = int(str(part_int) * count_rep)

    # decrement full number until its within the range
    while full_int > max_val:
        part_int -= 1
        full_int = int(str(part_int) * count_rep)

    total = 0

    # decrement and count full numbers within the range
    while min_val <= full_int:
        # increment total if not in seen
        if full_int not in seen:
            total += full_int
            seen.add(full_int)

        # update full num
        part_int -= 1
        full_int = int(str(part_int) * count_rep)

    return total


sum_two_reps = 0
sum_all_reps = 0

for num_a, num_b in id_ranges:
    # get sum in given range for ids that have 2 repeating numbers
    sum_two_reps += sum_invalid_ids(num_a, num_b, 2, seen=set())

    # get sum in given range for ids that have 2-[len of num_b] repeating numbers
    seen = set()  # ensure duplicates are not counted in sum
    for count_reps in range(2, len(str(num_b)) + 1):
        sum_all_reps += sum_invalid_ids(num_a, num_b, count_reps, seen)

print("Problem 1", sum_two_reps)
print("Problem 2", sum_all_reps)
