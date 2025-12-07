# read the input
# input_file = "D4_input_test.txt"
input_file = "D4_input.txt"

paper_indices = set()  # (row, col)
with open(input_file) as file:
    for row, line in enumerate(file):
        for col, ch in enumerate(line):
            if ch != "@":
                continue

            paper_indices.add((row, col))


# all eight directions
adjacent = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, -1), (-1, -1), (1, 1)]


def count_adjacent(row: int, col: int) -> int:
    count = 0
    for r, c in adjacent:
        if (row + r, col + c) in paper_indices:
            count += 1
    return count


def attempt_removal() -> int:
    remove = []

    for row, col in paper_indices:
        if count_adjacent(row, col) < 4:
            remove.append((row, col))  # save indices to remove paper

    # remove paper
    for row, col in remove:
        paper_indices.remove((row, col))

    return len(remove)


first_removal = 0
total_removal = 0

while True:
    count_removed = attempt_removal()
    if count_removed == 0:
        break  # no more iterations needed

    if first_removal == 0:
        first_removal = count_removed

    total_removal += count_removed

print("Problem 1", first_removal)
print("Problem 2", total_removal)
