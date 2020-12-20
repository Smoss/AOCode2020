from collections import defaultdict
input_file = open('Inputs/Input_5.txt', 'r')
high_id = 0
taken_ids = set()
for line in input_file:
    if not line:
        continue
    row, column = line[:7], line[7:-1]
    row_id = 0
    column_id = 0
    idx = 64
    for char in row:
        if char == 'B':
            row_id += idx
        idx //= 2
    idx = 4
    for char in column:
        if char == 'R':
            column_id += idx
        idx //= 2
    seat_id = 8 * row_id + column_id
    taken_ids.add(seat_id)
    high_id = max(high_id, seat_id)
options = set(range(min(taken_ids), high_id + 1)) - taken_ids
print(high_id)
print(options)