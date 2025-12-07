# read the input
# input_file = "D3_input_test.txt"
input_file = "D3_input.txt"


def select_top_digits(nums, count_digits: int):
    number = ""
    start = 0
    N = len(nums)

    for remaining in range(count_digits, 0, -1):
        # can only select new numbers before this index
        end = N - remaining + 1

        # find index of max digit in nums[start:end] and append to number
        max_i = max(range(start, end), key=lambda i: nums[i])
        number += str(nums[max_i])

        # can only select numbers after this index
        start = max_i + 1

    return int(number)


top_2 = 0
top_12 = 0

with open(input_file) as file:
    for line in file:
        nums = list(int(num) for num in line if num != "\n")
        top_2 += select_top_digits(nums, 2)  # choose top 2 digits
        top_12 += select_top_digits(nums, 12)  # choose top 12 digits

print("Problem 1", top_2)
print("Problem 2", top_12)
