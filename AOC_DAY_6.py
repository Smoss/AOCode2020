from collections import defaultdict
import string
input_file = open('Inputs/Input_6.txt', 'r')
curr_group = set()
all_yes = set(string.ascii_lowercase)
tot = 0
tot_yes = 0
for line in input_file:
    line = line.strip('\n')
    if not line:
        # print('####')
        tot += len(curr_group)
        tot_yes += len(all_yes)
        curr_group = set()
        all_yes = set(string.ascii_lowercase)
        continue
    # print(all_yes, set(line), all_yes.intersection(set(line)))
    curr_group = curr_group.union(set(line))
    all_yes = all_yes.intersection(set(line))

tot += len(curr_group)
curr_group = set()
tot_yes += len(all_yes)
print(tot, tot_yes)