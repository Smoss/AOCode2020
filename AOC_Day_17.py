from collections import defaultdict
import string, re
from math import cos, sin, pi
input_file = open('Inputs/Input_17.txt', 'r')
cubes = defaultdict(lambda : False)
min_x, max_x = -1, 1
min_y, max_y = -1, 1
min_z, max_z = -1, 1
min_w, max_w = -1, 1
for idx_i, row in enumerate(input_file):
    row = row.strip('\n')
    if row:
        for idx_j, val in enumerate(row):
            if val == '#':
                cubes [(idx_j, idx_i, 0, 0)] = True
                max_x = max(idx_j + 1, max_x)
                max_y = max(idx_i + 1, max_y)
print(cubes)
for _ in range(6):
    new_cubes = defaultdict(lambda : False)
    idx = 0
    print('#####')
    print(min_x, min_y, min_z, max_x, max_y, max_z)
    for x in range(min_x, max_x + 2):
        for y in range(min_y, max_y + 2):
            for z in range(min_z, max_z + 2):
                for w in range(min_w, max_w + 2):
                    active_count = 0
                    inactive_count = 0
                    curr_loc = (x, y, z, w)
                    # print(curr_loc)
                    for adj_x in range(x - 1, x + 2):
                        for adj_y in range(y - 1, y + 2):
                            for adj_z in range(z - 1, z + 2):
                                for adj_w in range(w - 1, w + 2):
                                    loc = (adj_x, adj_y, adj_z, adj_w)
                                    if curr_loc != loc:
                                        if cubes[loc]:
                                            active_count += 1
                                        else:
                                            inactive_count += 1
                    # print(max_z, min_z, z)
                    idx += 1
                    if cubes[curr_loc] and active_count in [2, 3]:
                        new_cubes[curr_loc] = True
                    elif not cubes[curr_loc] and active_count == 3:
                        new_cubes[curr_loc] = True
    cubes = new_cubes
    for key, val in cubes.items():
        if val:
            x, y, z, w = key
            max_x = max(x + 1, max_x)
            max_y = max(y + 1, max_y)
            max_z = max(z + 1, max_z)
            max_w = max(w + 1, max_w)
            min_x = min(x - 1, min_x)
            min_y = min(y - 1, min_y)
            min_z = min(z - 1, min_z)
            min_w = min(z - 1, min_w)
print(len(cubes.keys()))
