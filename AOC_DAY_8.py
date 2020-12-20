from collections import defaultdict
import string
input_file = open('Inputs/Input_8.txt', 'r')
instructions = [line.strip('\n').split(' ') for line in input_file if len(line) > 1]
# print(instructions[8])
def execute_code(instructions):
    accumulator = 0
    idx = 0
    indexes = set()
    while idx < len(instructions):
        # print(idx, instructions[idx])
        inst, val = instructions[idx]
        indexes.add(idx)
        val = int(val)
        if inst == 'jmp':
            idx += val
        else:
            if inst == 'acc':
                accumulator += val
            idx += 1
        if idx in indexes:
            return accumulator, False
    return accumulator, True
print(execute_code(instructions))
for i in range(len(instructions)):
    if instructions[i][0] == 'acc':
        continue
    # print(i)
    new_inst = [inst for inst in instructions]
    inst, val = new_inst[i]
    # print(inst, val)
    # print(new_inst[i])
    if inst == 'nop':
        inst = 'jmp'
    else:
        inst = 'nop'
    new_inst[i] = inst, val
    acc, passed = execute_code(new_inst)
    # print(acc, passed)
    if passed:
        print(acc)
        break
# idx = 0
# old_idx = 0
# accumulator = 0
# indexes = set()
# while idx < len(instructions):
#     print('idx: ', idx)
#     old_idx = idx
#     inst, val = instructions[idx]
#     indexes.add(idx)
#     val = int(val)
#     if inst == 'jmp':
#         idx += val
#     else:
#         if inst == 'acc':
#             accumulator += val
#         idx += 1
# print(accumulator)