import numpy as np
import pandas as pd
from tqdm import tqdm

INPUT = "test_input.txt"
# INPUT = "input.txt"

with open(INPUT, "r") as f:
    data = f.read().strip().split("\n")

# target_col = 2000000
target_col = 10

# def boundary(xy, sensors, beacons):
    # # breakpoint()
    # within = False
    # # xy = np.array((x, y))
    # # for s, b in zip(sensors,beacons):
    # for i in range(len(sensors)):
        # s, b = sensors[i], beacons[i]
        # # print(s, b)
        # # s, b = np.array(s), np.array(b)
        # if (s==b).all() :
            # break
        # boundary = np.linalg.norm(b-s, ord=1)
        # # boundary = 0
        # dist = np.linalg.norm(xy-s, ord=1)
        # # print(dist, boundary)
        # # print(dist < boundary)
        # if dist <= boundary:
            # within =  True
            # break
        # else:
            # within = False

    # return within

# def boundary(sensors, beacons):
    # # breakpoint()
    # bounds = []
    # for s, b in zip(sensors,beacons):
        # boundary = np.linalg.norm(b-s, ord=1)
        # boundary = int(boundary)
        # bounds.append(boundary)
    # return bounds
        
sensors = []
beacons = []
for d in data:
    d = d.split(" ")
    x, y = d[2].rstrip(","), d[3].rstrip(":")
    x, y = int(x[2:]), int(y[2:])
    sensors.append((x, y))
    x, y = d[8].rstrip(","), d[9]
    x, y = int(x[2:]), int(y[2:])
    beacons.append((x, y))

s_arr = np.array(sensors)
b_arr = np.array(beacons)
s_min = s_arr.min()
s_max = s_arr.max() 
b_min = b_arr.min()
b_max = b_arr.max() 
target_size = max(s_max, b_max) - min(s_min, b_min)
_max = max(s_max, b_max)
_min = min(s_min, b_min)
target = np.arange(_min, _max+1)
df = pd.Series(index=target, dtype=bool)
df[:] = False
ys = np.array([target_col]*len(target))
# target = np.column_stack((target, ys))

ts = np.zeros(target.shape, dtype=int)
# bounds = boundary(s_arr, b_arr)
i = 0
# TODO: profile to figure out, where the bottleneck is
# avoid computing bounds again
# replace np.linalg.norm with delta_x + delta_y
delta_b = b_arr - s_arr
# delta_b = b_arr - s_arr + 1
norms = np.linalg.norm(delta_b, ord=1, axis=1)
# breakpoint()
# delta_t = ts - s_arr
def get_inbounds(sensors, norms, target_col):
    # breakpoint()
    heights = sensors[:, 1] + norms
    depths = sensors[:, 1] - norms
    # bounds = np.column_stack((heights, depths))
    inbounds = np.where(
            (target_col<=heights) & (depths<=target_col),
            True, False
            ) 
    return inbounds
def set_values(df, sensors, norms, target_col):
    dfc = df.copy()
    dists = sensors[:, 1] - target_col
    dists = np.abs(dists)
    distant_bounds = 2*norms - 2*dists
    distant_bounds = distant_bounds.astype(int)
    for s, b in zip(sensors[:, 0], distant_bounds):
        left = s - distant_bounds // 2
        right = s + distant_bounds // 2
    for l, r in zip(left, right):
        dfc[l:r+1] = True
    # print(sum(df)*2)
    # print(sum(df))
    return dfc


target_col = 0
inbounds = get_inbounds(s_arr, norms, target_col)
dfcc = df.copy()
for target_col in range(25):
    # breakpoint()
    dfc = set_values(df, s_arr[inbounds], norms[inbounds], target_col)
    dfcc = pd.concat((dfcc, dfc), axis=1)
print(dfcc)
# for t in tqdm(target):
    # if boundary(t, s_arr, b_arr):
        # # ts.append(t)
        # ts[i] = 1
    # i += 1


# print(len(ts))
print(sum(ts))
# breakpoint()

