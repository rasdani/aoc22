import numpy as np

# INPUT = "test_input.txt"
# INPUT = "input.txt"
INPUT = "larger_example.txt"

with open(INPUT, "r") as f:
    data = f.read().strip().split("\n")


# if only I had updated to Python 3.10 ...
# one could refactor using np.sum(h-t) == 2 etc.
def move_t(h, t):
    # FIX ME: after fist move 6 to 9 are left at (0,0)
    # breakpoint()
    if (h-t == [2, 0]).all():
        t[0] += 1
    elif (h-t == [-2,0]).all():
        t[0] -= 1
    elif (h-t == [0, 2]).all():
        t[1] += 1
    elif (h-t == [0, -2]).all():
        t[1] -= 1
    elif (h-t == [1, 2]).all():
        t += [1, 1]
    elif (h-t == [-1, 2]).all():
        t += [-1, 1]
    elif (h-t == [1, -2]).all():
        t += [1, -1]
    elif (h-t == [-1, -2]).all():
        t += [-1, -1]
    elif (h-t == [-2, 1]).all():
        t += [-1, 1]
    elif (h-t == [2, 1]).all():
        t += [1, 1]
    elif (h-t == [2, -1]).all():
        t += [1, -1]
    elif (h-t == [-2, -1]).all():
        t += [-1, -1]

    # print(t)
    return t

# def move(d, n, t, visited):
def move(d, n, knots, visited):
    breakpoint()
    for _ in range(n):
        if d=="R":
            knots[0][0] += 1
            for key in range(9):
                knots[key+1] = move_t(knots[key], knots[key+1])
            # t = move_t(h, t)
            # visited.append(tuple(t))
            visited.append(tuple(knots[9]))
        elif d=="L":
            knots[0][0] -= 1
            for key in range(9):
                knots[key+1] = move_t(knots[key], knots[key+1])
            # t = move_t(h, t)
            # visited.append(tuple(t))
            visited.append(tuple(knots[9]))
        elif d=="U":
            knots[0][1] += 1
            for key in range(9):
                knots[key+1] = move_t(knots[key], knots[key+1])
            # t = move_t(h, t)
            # visited.append(tuple(t))
            visited.append(tuple(knots[9]))
        elif d=="D":
            knots[0][1] -= 1
            for key in range(9):
                knots[key+1] = move_t(knots[key], knots[key+1])
            # t = move_t(h, t)
            # visited.append(tuple(t))
            visited.append(tuple(knots[9]))
        else:
            raise Exception

    screen = np.zeros((25, 25))
    for key, value in knots.items():
        screen[value[0]+5, value[1]+12] = key
    print(screen.T)
    # print(visited[-1])
    return visited

knots = {key: np.array((0,0)) for key in range(10)}
h = (0, 0)
t = (0, 0)
h = np.array(h)
t = np.array(t)
visited = []
v = []
for inst in data:
    d, n = inst.split(" ")
    n = int(n)
    print(d, n)
    # visited = move(d,n, t, visited)
    visited = move(d,n, knots, visited)
    v.append(set(visited))

print(set(visited))
print(len(set((visited))))

breakpoint()
