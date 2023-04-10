import numpy as np
INPUT = "input.txt"

with open(INPUT, "r") as f:
    data = f.read().strip().split("\n")

def print_arr(arr):
    ret = ""
    for row in arr:
        for r in row:
            ret += str(r).zfill(3) + " "
        ret += "\n"
    print(ret)

def loss(arr, xy, start=(20, 0)):
    # breakpoint()
    x, y = xy
    l1 = np.array(xy) - np.array(start)
    l1 = np.linalg.norm(l1, ord=1)
    alti = arr[x, y]
    return int(l1 + alti)

def argmin(arr):
    flat_idx = np.argmin(arr)
    return np.unravel_index(flat_idx, arr.shape)

def apply_loss(arr):
    # arr unfortunately not quadratic
    ret = np.zeros(arr.shape, dtype=int)
    rows, cols = arr.shape
    for r in range(rows):
        for c in range(cols):
            ret[r, c] = loss(arr, (r,c))

    return ret

def descent(arr, top=(20, 36)):
    # TODO: only consider steps which decrease by one!
    l = np.inf
    x, y = top
    up = arr[x-1 , y]
    down = arr[x+1 , y]
    right = arr[x , y+1]
    left = arr[x , y-1]
    # while l >

    


row = [ord(x)-96 for x in data[0]]
arr = np.array(row)
# TODO: optimize joint loss of l1-norm and altitude, descent from top
for row in data[1:]:
    row = [ord(x)-96 if x!="S" else 0 for x in row ]
    row = np.array(row)
    arr = np.vstack([arr, row])

l_arr = apply_loss(arr)
print_arr(l_arr)
breakpoint()
