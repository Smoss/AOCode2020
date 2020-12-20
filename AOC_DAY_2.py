from collections import defaultdict
input_file = open('Inputs/Input_2.txt', 'r')
valid_counts = 0
valid_indexes = 0
for val in input_file:
    policy, pw = val.split(':')
    counts, target = policy.split(' ')
    lo, hi = counts.split('-')
    counts = defaultdict(int)
    for char in pw:
        counts[char] += 1
    final_count = counts[target]
    if final_count >= int(lo) and final_count <= int(hi):
        valid_counts += 1
    if target in [pw[int(lo)], pw[int(hi)]] and pw[int(lo)] != pw[int(hi)]:
        valid_indexes += 1


print(valid_counts)
print(valid_indexes)