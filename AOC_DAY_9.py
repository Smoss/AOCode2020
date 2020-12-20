from collections import defaultdict
import string
input_file = open('Inputs/Input_9.txt', 'r')
numbers = [int(line.strip('\n')) for line in input_file if len(line) > 1]
preamble = numbers[:25]
val = 0
for num in numbers[25:]:
    found = False
    for idx, val_1 in enumerate(preamble):
        for val_2 in preamble[idx + 1:]:
            if val_1 + val_2 == num:
                found = True
    if not found:
        val = num
        print(num)
        break
    preamble.pop(0)
    preamble.append(num)

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers) + 1):
        vals = numbers[i:j]
        if sum(vals) == val:
            print(min(vals) + max(vals))
            exit()
