import numpy as np

# INPUT = "test_input.txt"
INPUT = "input.txt"

with open(INPUT, "r") as f:
    data = f.read().strip().split("\n")

def signal(cycle, X):
    if cycle==20 or (cycle-20) % 40 == 0:
        print(cycle * X)
        return(cycle * X)

def draw(cycle, sprite):
    ret = ""
    cycle = cycle % 40
    if cycle in sprite:
        ret += "#"
    else:
        ret += "."

    if cycle == 0:
        ret += "\n"

    return ret


X = 1
cycle = 0
signals = []
sprite  = np.array([1, 2, 3])
screen = ""
for d in data:
    try:
        inst, value = d.split(" ")
        value = int(value)
    except ValueError:
        inst = d
    if inst == "addx":
        for _ in range(2):
            cycle += 1
            # s = signal(cycle, X)
            # if s: signals.append(s)
            screen += draw(cycle, sprite)

        # X += value
        sprite += value
    else:
        cycle += 1
        # s = signal(cycle, X)
        # if s: signals.append(s)
        screen += draw(cycle, sprite)
        
# print(sum(signals))
print(screen)
