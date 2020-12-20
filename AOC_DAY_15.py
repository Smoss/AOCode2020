from collections import defaultdict
import string, re
from math import cos, sin, pi
input_file = [6,13,1,15,2,0]
memory = {i: idx + 1 for idx, i in enumerate(input_file)}
spoken = 0
print(memory)
for i in range(len(input_file) + 1, 30000000):
    if spoken in memory:
        # print('here')
        temp = memory[spoken]
        memory[spoken] = i
        spoken = i - temp
    else:
        memory[spoken] = i
        spoken = 0
    if i % 100000 == 0:
        print(i)
print(spoken)