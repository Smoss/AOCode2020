from collections import defaultdict
import string, re
from math import cos, sin, pi, sqrt
from operator import add, mul
input_file = open('Inputs/Input_20.txt', 'r')
tiles = input_file.read().split('\n\n')
tile_map = {}
for tile in tiles:
    tile_id, *lines = tile.split('\n')
    tile_id = int(tile_id.split(' ')[1][:-1])
    tile_map[tile_id] = lines
# print(len(tile_map.keys()))
tile_ids = set(tile_map.keys())
prod = 1
def get_borders(tile):
    top_line = tile[0]
    left_line = ''.join([row[0] for row in tile])
    bottom_line = tile[-1]
    right_line = ''.join([row[-1] for row in tile])
    ret_dict = {}
    pre_dict = {top_line: 'top', left_line: 'left', right_line: 'right', bottom_line: 'bot'}
    for rot, loc in pre_dict.items():
        ret_dict[rot[::-1]] = '{}_rev'.format(loc)
    ret_dict.update(pre_dict)
    return ret_dict
adjacency_map = defaultdict(set)
corners = []
for first_id in tile_ids:
    count = 0
    for second_id in tile_ids:
        if first_id == second_id:
            continue
        first_borders = get_borders(tile_map[first_id])
        second_borders = get_borders(tile_map[second_id])
        # print(first_id, second_id, len(first_borders.intersection(second_borders)))
        for rot, loc in first_borders.items():
            if rot in second_borders:
                count += 1
                adjacency_map[first_id].add(second_id)
                adjacency_map[second_id].add(first_id)
                break

    # print(first_id, count)
    if count == 2:
        corners.append(first_id)
        prod *= first_id
print(prod)
# print(adjacency_map)
# print(corners)
# curr_tiles = []
start_point = list(corners)[0]
adj_tiles = set(adjacency_map[start_point])
indices = [(0,2), (1,1), (2,0)]
# locs = {}
# locs[start_point] = (0, 0)
image = {}
def get_simple_borders(tile):
    top_line = tile[0]
    left_line = ''.join([row[0] for row in tile])
    bottom_line = tile[-1]
    right_line = ''.join([row[-1] for row in tile])
    pre_dict = {top_line: 'top', left_line: 'left', right_line: 'right', bottom_line: 'bottom'}
    return pre_dict
def flip_tile_hor(tile):
    return [row[::-1] for row in tile]
def flip_tile_vert(tile):
    return tile[::-1]
def rotate_tile(tile):
    new_tile = []
    # print(tile)
    for line in zip(*tile[::-1]):
        # print(len(line))
        new_tile.append(''.join(line))
    return new_tile
tile_ids.remove(start_point)
new_adj_tiles = []
visited_tiles = {start_point}
start_tile = tile_map[start_point]
image [(0, 0)] = start_tile
locs ={start_point: (0, 0)}
# print('\n'.join(start_tile))
# print()
# print('\n'.join(flip_tile_hor(start_tile)))
# for i in range(4):
#     print('\n'.join(tile))
#     print('---')
#     tile = rotate_tile(tile)
# print(start_point, adj_tiles)
dir_map = {'bottom': (0, 1), 'right': (1, 0), 'top': (0, -1), 'left': (-1, 0)}
rev_map = {'bottom':'top', 'right': 'left', 'top': 'bottom', 'left': 'right'}
# for tile_id in adj_tiles:
#     tile_ids.remove(tile_id)
#     visited_tiles.add(tile_id)
#     start_tile = image[(0, 0)]
#     new_adj_tiles += adjacency_map[tile_id]
#     sec_tile = tile_map[tile_id]
#     first_borders = get_simple_borders(start_tile)
#     second_borders = get_simple_borders(sec_tile)
#     first_set = set(first_borders.keys())
#     second_set = set(second_borders.keys())
#     while not first_set.intersection(second_set):
#         sec_tile = flip_tile_hor(sec_tile)
#         first_borders = get_simple_borders(start_tile)
#         second_borders = get_simple_borders(sec_tile)
#         first_set = set(first_borders.keys())
#         second_set = set(second_borders.keys())
#         if not first_set.intersection(second_set):
#             sec_tile = flip_tile_vert(sec_tile)
#             first_borders = get_simple_borders(start_tile)
#             second_borders = get_simple_borders(sec_tile)
#             first_set = set(first_borders.keys())
#             second_set = set(second_borders.keys())
#     first_match = first_borders[list(first_set.intersection(second_set))[0]]
#     second_match = second_borders[list(first_set.intersection(second_set))[0]]
#     d_x, d_y = dir_map[match]
#     image[(d_x, d_y)] = sec_tile
#     locs[tile_id] = (d_x, d_y)
#     print(match, start_point, tile_id)
print(locs)
def allMatch(new_borders, existing_borders):
    second_set = set(new_borders.keys())
    for border in existing_borders.values():
        first_set = set(border.keys())
        if not first_set.intersection(second_set):
            return False
    return True
# print(adj_tiles)
new_adj_tiles = adj_tiles
while tile_ids:
    adj_tiles = new_adj_tiles
    new_adj_tiles = []
    for tile_id in adj_tiles:
        new_tile = tile_map[tile_id]
        border_tiles = adjacency_map[tile_id].difference(tile_ids)
        border_locs = {locs[border_id] for border_id in border_tiles}
        # print(tile_id, border_tiles)
        # print([''.join(image[locs[border_id]]) == ''.join(tile_map[border_id]) in locs for border_id in border_tiles])
        existing_borders = {border_id: get_simple_borders(image[locs[border_id]]) for border_id in border_tiles}
        print(len(border_tiles))
        new_borders = get_simple_borders(new_tile)
        while not allMatch(new_borders, existing_borders):
            # print('here')
            new_tile = flip_tile_hor(new_tile)
            new_borders = get_simple_borders(new_tile)
            if not allMatch(new_borders, existing_borders):
                new_tile = rotate_tile(new_tile)
                new_borders = get_simple_borders(new_tile)
            if not allMatch(new_borders, existing_borders):
                new_tile = flip_tile_vert(new_tile)
                new_borders = get_simple_borders(new_tile)
            if not allMatch(new_borders, existing_borders):
                new_tile = rotate_tile(new_tile)
                new_borders = get_simple_borders(new_tile)
        new_set = set(new_borders.keys())
        # print(len(existing_borders))
        poss_locs = set()
        while len(poss_locs) != 1:
            # print(poss_locs)
            poss_locs = set()
            for border_id, border in existing_borders.items():
                existing_set = set(border.keys())
                print(border)
                first_match = border[list(existing_set.intersection(new_set))[0]]
                second_match = new_borders[list(existing_set.intersection(new_set))[0]]
                while first_match != rev_map[second_match]:
                    print(first_match, second_match)
                    if first_match == second_match:
                        new_tile = rotate_tile(new_tile)
                        new_tile = rotate_tile(new_tile)
                        if first_match in ['right', 'left']:
                            new_tile = flip_tile_vert(new_tile)
                        else:
                            new_tile = flip_tile_hor(new_tile)
                    elif first_match in ['top', 'bottom']:
                        new_tile = flip_tile_hor(new_tile)
                        new_tile = rotate_tile(new_tile)
                    else:
                        new_tile = flip_tile_vert(new_tile)
                        new_tile = rotate_tile(new_tile)
                    new_borders = get_simple_borders(new_tile)
                    new_set = set(new_borders.keys())
                    print(new_borders, border)
                    second_match = new_borders[list(existing_set.intersection(new_set))[0]]
                    # print(second_match)
                print(dir_map[first_match])
                poss_locs.add(dir_map[first_match])
        new_loc = list(poss_locs)[0]
        image[new_loc] = new_tile
        locs[tile_id] = new_loc
        new_adj_tiles += adjacency_map[tile_id]
        tile_ids.remove(tile_id)
    new_adj_tiles = set(new_adj_tiles).intersection(tile_ids)
    # break
print(new_adj_tiles)
print(image.keys())
# line_1 = re.compile(r'..................#.')
# line_2 = re.compile(r'#....##....##....###')
# line_3 = re.compile(r'.#..#..#..#..#..#...')
# while tile_ids:
#     break