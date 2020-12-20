from collections import defaultdict
import string
input_file = open('Inputs/Input_11.txt', 'r')
curr_round = []
next_round = [list(line.strip('\n')) for line in input_file]
adder = {'#': 1, 'L': 0}
def print_maybe(i, j, idx_i, idx_j, near):
    # return
    if i == 1 and j == 1:
        print(i, j, idx_i, idx_j, near)
vis = []
while next_round != curr_round:
    print('\n'.join([''.join(row) for row in curr_round]))
    print('```')
    # print('\n'.join([''.join(row) for row in next_round]))
    print('```')
    curr_round = next_round
    next_round = []
    vis = []
    for i, row in enumerate(curr_round):
        next_row = []
        next_vis =[]
        for j, seat in enumerate(row):
            if seat == '.':
                next_row.append('.')
                next_vis.append('.')
                continue
            near = 0
            # print(row)
            idx_i, idx_j = i, j
            if i > 0:
                idx_i = i - 1
                while idx_i >= 0:
                    if curr_round[idx_i][j] in ['#', 'L']:
                        near += adder[curr_round[idx_i][j]]
                        break
                    idx_i -= 1
                print_maybe(i, j, idx_i, idx_j, near)
                if j > 0:
                    idx_i, idx_j = i - 1, j - 1
                    while idx_i >= 0 and idx_j >= 0:
                        if curr_round[idx_i][idx_j] in ['#', 'L']:
                            near += adder[curr_round[idx_i][idx_j]]
                            break
                        idx_i -= 1
                        idx_j -= 1
                print_maybe(i, j, idx_i, idx_j, near)
                if j < len(row):
                    idx_i, idx_j = i - 1, j + 1
                    while idx_i >= 0 and idx_j < len(row):
                        if curr_round[idx_i][idx_j] in ['#', 'L']:
                            near += adder[curr_round[idx_i][idx_j]]
                            break
                        idx_i -= 1
                        idx_j += 1
                print_maybe(i, j, idx_i, idx_j, near)
            idx_i, idx_j = i, j
            if i < len(row):
                idx_i = i + 1
                while idx_i < len(curr_round):
                    if curr_round[idx_i][j] in ['#', 'L']:
                        near += adder[curr_round[idx_i][j]]
                        break
                    idx_i += 1
                print_maybe(i, j, idx_i, idx_j, near)
                if j > 0:
                    idx_i, idx_j = i + 1, j - 1
                    while idx_i < len(curr_round) and idx_j >= 0:
                        if curr_round[idx_i][idx_j] in ['#', 'L']:
                            near += adder[curr_round[idx_i][idx_j]]
                            break
                        idx_i += 1
                        idx_j -= 1
                print_maybe(i, j, idx_i, idx_j, near)
                if j < len(row):
                    idx_i, idx_j = i + 1, j + 1
                    while idx_i < len(curr_round) and idx_j < len(row):
                        if curr_round[idx_i][idx_j] in ['#', 'L']:
                            near += adder[curr_round[idx_i][idx_j]]
                            break
                        idx_i += 1
                        idx_j += 1
                print_maybe(i, j, idx_i, idx_j, near)
            if j > 0:
                idx_j = j - 1
                while idx_j >= 0:
                    if curr_round[i][idx_j] in ['#', 'L']:
                        near += adder[curr_round[i][idx_j]]
                        break
                    idx_j -= 1
            print_maybe(i, j, idx_i, idx_j, near)
            if j < len(row):
                idx_j = j + 1
                while idx_j < len(row):
                    if curr_round[i][idx_j] in ['#', 'L']:
                        near += adder[curr_round[i][idx_j]]
                        break
                    idx_j += 1
            print_maybe(i, j, idx_i, idx_j, near)
            if seat == 'L' and near == 0:
                next_row.append('#')
            elif seat == '#' and near >= 5:
                next_row.append('L')
            else:
                next_row.append(seat)
            next_vis.append(str(near))
            # if i == 0 and j == 0:
            #     print(near)
        next_round.append(next_row)
        vis.append(next_vis)
    # print('\n'.join([''.join(row) for row in vis]))
# print(curr_round)
tot = 0
for row in curr_round:
    for seat in row:
       if seat == '#':
           tot += 1
print(tot)