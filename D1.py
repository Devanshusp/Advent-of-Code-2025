# read the input
# input_file = "advent_of_code/D1_input_test.txt"
input_file = "advent_of_code/D1_input.txt"

# positions
limit_pos = 100  # 0-99
current_pos = 50  # starts at pos 50
count_pos_zero = 0  # how many times each turn ends at pos 0
count_rot_zero = 0  # how many times the lock makes contact with pos 0

with open(input_file) as file:
    for line in file:
        _start_pos = current_pos

        match line[0]:
            case "L":
                # move to smaller nums
                current_pos -= int(line[1:])
            case "R":
                # move to larger nums
                current_pos += int(line[1:])
            case _:
                raise Exception(f"input should only contain L[num] and R[num], not: {line}")

        _end_pos = current_pos

        # calc times lock made contact with pos 0
        count_rot_zero += abs(current_pos) // limit_pos  # count full turns
        if (_start_pos > 0 and _end_pos < 0) or _end_pos == 0:  # 1st turn across 0 or lands on 0
            count_rot_zero += 1

        # save times lock lands on pos 0
        current_pos %= limit_pos
        if current_pos == 0:
            count_pos_zero += 1

print("Problem 1", count_pos_zero)
print("Problem 2", count_rot_zero)
