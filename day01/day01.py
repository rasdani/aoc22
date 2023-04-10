from itertools import groupby

INPUT_FILE = "test_input.txt"
# INPUT_FILE = "input.txt"

f = open(INPUT_FILE, "r")
f = f.read()
f = f.splitlines()

bags = [list(sub) for key, sub in groupby(f, key=bool) if key]

### First half ###
# max_calories = 0
# for bag in bags:
    # bag = [int(x) for x in bag]
    # calories = sum(bag)
    # if calories > max_calories:
        # max_calories = calories
        
# print(max_calories)


### Second half ###
sums = []
for bag in bags:
    calorie_sum = sum([int(x) for x in bag])
    sums.append(calorie_sum)

res = sorted(sums)
res = sum(res[-3:])
# print(sums)
# print(sorted(sums))
print(res)
