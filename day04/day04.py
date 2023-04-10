# INPUT = "test_input.txt"
INPUT = "input.txt"

with open(INPUT, "r") as f:
    data = f.read().splitlines()

i = 0
for pair in data:
    first, second = pair.split(",")
    first_start, first_end = first.split("-")
    first_start, first_end = int(first_start), int(first_end)
    second_start, second_end = second.split("-")
    second_start, second_end = int(second_start), int(second_end)
    second_in_first = (first_start <= second_start and second_end <= first_end)
    first_in_second = (second_start <= first_start and first_end <= second_end)
    ### Part 2 ###
    first_set = set(range(first_start, first_end+1))
    second_set = set(range(second_start, second_end+1))
    # if second_in_first or first_in_second:
    if first_set & second_set:    # Part 2
        i += 1

print(i)
