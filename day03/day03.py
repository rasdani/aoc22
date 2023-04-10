# INPUT = "../test_input.txt"
INPUT = "input.txt"

with open(INPUT, "r") as f:
    data = f.read()

data = data.splitlines()

commons = []
for line in data:
    length = len(line)
    assert length % 2 == 0
    mid = length // 2
    first, second = line[:mid], line[mid:]
    assert len(first) == len(second)
    intersection = set(first) & set(second)
    commons.append(*intersection)

prios = [ord(x)-96 if x.islower() else ord(x)-38 for x in commons]
res = sum(prios)
# print(res)

### Part 2 ###
assert len(data) % 3 == 0
iters = [iter(data)] * 3
iters = zip(*iters)
chunks = [list(i) for i in iters]

badges = []
for chunk in chunks:
    first, second, third = chunk
    intersection = set(first) & set(second) & set(third)
    badges.append(*intersection)

prios = [ord(x)-96 if x.islower() else ord(x)-38 for x in badges]
res = sum(prios)
print(res)
