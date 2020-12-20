from collections import defaultdict
import string
input_file = open('Inputs/Input_10.txt', 'r')
jolts = [int(line.strip('\n')) for line in input_file if line.strip('\n')]
jolts = sorted(jolts)
max_joltage = jolts[-1] + 3
print(max_joltage)
idx = 0
ones = 0
threes = 1
ways = {0: 1}
for idx_j, jolt in enumerate(jolts):
    paths = 0
    for i in range(max(0, jolt - 3), jolt):
        paths += ways.get(i, 0)
    ways[jolt] = paths
    if jolt - idx == 1:
        ones += 1
    elif jolt - idx == 3:
        threes += 1
    idx = jolt

# prod =
# for paths in ways.values():
#     prod *= len(paths)
print(ones * threes)
print(ways[jolts[-1]])