import numpy as np
INPUT = "test_input.txt"
# INPUT = "input.txt"

with open(INPUT, "r") as f:
    data = f.read().splitlines()

dat = []
for d in data:
    s = []
    for c in d:
        s.append(c)
    dat.append(s)

arr = np.array(dat, dtype="int")

# boundary = arr.shape[0]*2 + (arr.shape[1]-2)*2

rows, cols = arr.shape

# for r in range(rows):

def boundary(arr):
    rows, cols = arr.shape
    # arr[0,] = np.ones(cols)
    # arr[-1,] = np.ones(cols)
    # arr[:,0] = np.ones(cols)
    # arr[:,-1] = np.ones(cols)
    arr[0,] = np.zeros(cols)
    arr[-1,] = np.zeros(cols)
    arr[:,0] = np.zeros(cols)
    arr[:,-1] = np.zeros(cols)

# def visible(arr, arr2):
    # # breakpoint()
    # rows, cols = arr.shape
    # for r, line in enumerate(arr):
        # # if r==2:
            # # breakpoint()
        # # print(line)
        # tallest = line[0]
        # for c in range(cols-1):
            # if tallest < line[c+1]:
                # tallest = line[c+1]
                # arr2[r, c+1] = 1
    # # breakpoint()

# def visible(arr, arr2):
    # breakpoint()
    # rows, cols = arr.shape
    # for r, line in enumerate(arr):
        # # if r==2:
            # # breakpoint()
        # # print(line)
        # tallest = line[0]
        # counter = 0
        # for c in range(cols-1):
            # if tallest <= line[c+1]:
                # tallest = line[c+1]
                # counter += 1
                # arr2[r, c+1] = arr2[r,c+1] * counter
                # counter = 1
            # else:
                # counter += 1
                # arr2[r, c+1] = arr2[r,c+1] * counter
    # breakpoint()

def visible(arr, arr2):
    breakpoint()
    rows, cols = arr.shape
    for i , tallest in enumerate(arr[1:-1, 0]):
        dist = 0
        # r = i
        for c in range(cols):
            dist += 1
            if arr[i, c] == tallest:
                if i==0:
                    dist = 0
                pass
            elif tallest < arr[i, c]:
                arr2[i, c] *= dist
                tallest = arr[i, c]
            elif arr[i, c] < tallest:
                arr2[i, c] *= dist
            else:
                print("MISSED CASE")
                print(tallest, arr[i, c])

            # if tallest <= arr[r, c]:
                # arr2[r, c] *= dist
                # tallest = arr[r, c]
                # # if arr[r, c-1] == tallest:
                    # # dist = 0
            # elif arr[r, c-1] == tallest:
                # dist = 0
                # # arr2[r, c] *= dist
            # else:
                # arr2[r, c] *= dist

    breakpoint()



                




# breakpoint()
# bits = np.zeros(arr.shape)
bits = np.ones(arr.shape)
boundary(bits)
visible(arr, bits)
visible(arr[:, ::-1], bits[:, ::-1])
visible(arr.T, bits.T)
visible(arr.T[:, ::-1], bits.T[:, ::-1])
# print(sum(sum(bits)))
print(np.max(bits))
breakpoint()
