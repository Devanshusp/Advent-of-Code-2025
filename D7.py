from functools import cache

# read the input
# input_file = "D7_input_test.txt"
input_file = "D7_input.txt"

splitters: list[set] = []
beam_index = -1

with open(input_file) as file:
    beam_index = file.readline().find("S")

    for line in file:
        split_indices = set(i for i, ch in enumerate(line) if ch == "^")
        if split_indices:
            splitters.append(split_indices)


def count_splits(beam_indices: set, splitter_row: int, count: int) -> int:
    # base case 1: no more rows -> done splitting
    if splitter_row >= len(splitters):
        return count

    # recursive case 2: attempt splitting on this row, count splits, and move to next row
    _beam_indices = set()

    for i in beam_indices:
        if i in splitters[splitter_row]:
            count += 1  # new split
            _beam_indices.add(i - 1)  # left
            _beam_indices.add(i + 1)  # right
        else:
            _beam_indices.add(i)  # keep same index

    return count_splits(_beam_indices, splitter_row + 1, count)  # tail-recursion


@cache
def count_decisions(beam_index: int, splitter_row: int) -> int:
    # base case 1: no more rows -> done splitting
    if splitter_row >= len(splitters):
        return 0

    # recursive case 2: beam doesn't split in this row -> move to next row
    if beam_index not in splitters[splitter_row]:
        return count_decisions(beam_index, splitter_row + 1)

    # recursive case 3: beam splits -> count divs @ left index and right index
    count_left = count_decisions(beam_index - 1, splitter_row + 1)
    count_right = count_decisions(beam_index + 1, splitter_row + 1)
    return 1 + count_left + count_right


print("Problem 1", count_splits({beam_index}, 0, 0))
print("Problem 2", 1 + count_decisions(beam_index, 0))
