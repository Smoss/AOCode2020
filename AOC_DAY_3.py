from collections import defaultdict
input_file = open('Inputs/Input_3.txt', 'r')
hill = [row.strip('\n') for row in input_file]
# idx = 0
max_len = len(hill[0])
# print(hill[0][-1])

def traverse_hill(right, down, hill):
    idx = 0
    collisions = 0
    # print(right, down)
    for row in hill[::down]:
        if row[idx] == '#':
            collisions += 1
        idx = (idx + right) % max_len
    # print(events)
    return collisions

collisions = traverse_hill(3, 1, hill)
print(collisions)
prod = collisions
# collisions = 0
slopes = [(1,1), (5,1), (7,1), (1,2)]
for right, down in slopes:
    prod *= traverse_hill(right, down, hill)
print(prod)
