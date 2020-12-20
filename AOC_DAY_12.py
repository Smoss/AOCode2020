from collections import defaultdict
import string
from math import cos, sin, pi
input_file = open('Inputs/Input_12.txt', 'r')
pos = (0, 0)
facing = 0
mult = {'L': 1, 'R': -1}
dirs = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}
for line in input_file:
    line = line.strip('\n')
    if not line:
        continue
    dir, dist = line[0], int(line[1:])
    pos_x, pos_y = pos
    if dir in ['L', 'R']:
        facing = (facing + dist * mult[dir]) % 360
    elif dir in ['N', 'S', 'W', 'E']:
        pos = (pos_x + dist * dirs[dir][0], pos_y + dist * dirs[dir][1])
    else:
        dist_x, dist_y = cos(facing * pi / 180) * dist, sin(facing * pi / 180) * dist
        # print(dist_x, dist_y, sin(3 * pi / 2))
        pos = (pos_x + dist_x), (pos_y + dist_y)
    # print(line, facing, pos)
# print(pos)
pos = (0, 0)
waypoint = (10, 1)
facing = 0
mult = {'L': 1, 'R': -1}
dirs = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}
input_file = open('Inputs/Input_12.txt', 'r')
for line in input_file:
    line = line.strip('\n')
    if not line:
        continue
    dir, dist = line[0], int(line[1:])
    pos_x, pos_y = pos
    way_x, way_y = waypoint
    if dir in ['L', 'R']:
        rot = dist * mult[dir] * pi / 180
        new_x, new_y = way_x * cos(rot) - way_y * sin(rot), way_y * cos(rot) + way_x * sin(rot)
        waypoint = new_x, new_y
    elif dir in ['N', 'S', 'W', 'E']:
        waypoint = (way_x + dist * dirs[dir][0], way_y + dist * dirs[dir][1])
    else:
        dist_x, dist_y = way_x * dist, way_y * dist
        # print(dist_x, dist_y, sin(3 * pi / 2))
        pos = (pos_x + dist_x), (pos_y + dist_y)
    print(line, facing, pos)