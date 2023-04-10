import re
from itertools import groupby

# INPUT = "test_input.txt"
INPUT = "input.txt"

with open(INPUT, "r") as f:
    data = f.read().splitlines()

data = [list(sub) for key, sub in groupby(data, key=bool) if key]
crates, proc = data

# figure out how to repeat properly
regex = "^(.{3})\s(.{3})\s(.{3})\s(.{3})\s(.{3})\s(.{3})\s(.{3})\s(.{3})\s(.{3})" 
# regex = "^(.{3})\s(.{3})\s(.{3})"    # for test_input.txt

def read_crates(crates):
    for i, line in enumerate(crates[:-1], 1):
        crate_line = re.findall(regex, line)
        if i == 1:
            d = {key: [value] for key, value in enumerate(*crate_line, 1)}

        else:
            for j, c in enumerate(*crate_line, 1):
                d[j].append(c)
    return d
               
def read_proc(proc):
    n = []
    _from = []
    to = []
    for i, line in enumerate(proc):
        line = line.split(" ")
        n.append(line[1])
        _from.append(line[3])
        to.append(line[5])
    return n, _from, to

def move(d, n, _from, to):
    d = {key: value[::-1] for key, value in d.items()}
    for key, value in d.items():
        clean = [x for x in value if x != "   "]
        d[key] = clean

    for _n ,f, t in zip(n, _from, to):
        _n, f, t = int(_n), int(f), int(t)
        tomove = d[f][-_n:]
        del d[f][-_n:]
        # d[t] = d[t] + tomove[::-1]
        d[t] = d[t] + tomove    # Part 2
    ret = [value.pop() for value in d.values()]
    print(ret)


d = read_crates(crates)
n, _from, to = read_proc(proc)
move(d, n, _from, to)
