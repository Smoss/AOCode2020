from collections import defaultdict
import string
from math import cos, sin, pi
from functools import reduce

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    # print(prod)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

input_file = open('Inputs/Input_13.txt', 'r')
timestamp = int(input_file.readline())
event_line = input_file.readline().strip('\n').split(',')
events = sorted([int(line.strip('\n'))for line in event_line if line and 'x' not in line])
times = {idx: int(line) for idx, line in enumerate(event_line) if line and 'x' not in line}
orders = sorted(times.keys())
start = timestamp
breaker = True
while breaker:
    for event in events:
        if start % event == 0:
            print((start - timestamp) * event)
            breaker = False
    start += 1
print([times[time] for time in orders], [-order for order in orders])
print(chinese_remainder([times[time] for time in orders], [-order for order in orders]))
# def calc_next(basis, targ):
#     t = 0
#     r = targ
#     newt = 1
#     newr = basis
#     while newr != 0:
#         # print(newr)
#         quotient = r // newr
#         (t, newt) = (newt, t - quotient * newt)
#         (r, newr) = (newr, r - quotient * newr)
#
#     # print(r)
#     if r > 1:
#         return "a is not invertible"
#     if t < 0:
#         t = t + targ
#     return t
#
def check_true(time_stamp, times):
    for idx, event in times.items():
        print(idx, event)
        if (time_stamp + idx) % event != 0:
            return False
    return True
print(check_true(chinese_remainder([times[time] for time in orders], orders), times))
#
# # max_event = max(events)
# # index = event_line.index(str(max_event)) + 1
# key_val = int(event_line[0])
# timestamp = 0
# # w
# new_times = []
# prev_index = 0
# prelim_basis = int(times[0])
# prod = 1
# for index in orders[1:]:
#     print(index, prev_index)
#     curr_index = index - prev_index
#     # for sub_index in orders[idx + 1:]:
#     # print(index, int(times[index]), prelim_basis, calc_next(int(times[index]), prelim_basis))
#     #     print()
#     # prod *= (index * calc_next(int(times[index]), prelim_basis))
#     # new_times.append((index * calc_next(int(times[index]), prelim_basis) * int(times[index]), int(times[index]) + 1))
#     timestamp = curr_index * calc_next(int(times[index]), prelim_basis) * prod * times[index]
#     prod *= (times[prev_index] + 1)
#     prev_index = index
#     print(timestamp, prod)
# print(timestamp)
# offsets = orders[1:]
# while len(offsets) > 1:
#     curr_times = new_times
#     new_times = []
#     prelim_basis = curr_times[0]
#     for index, tim in zip(offsets[1:], curr_times[1:]):
#         time =
#         # for sub_index in orders[idx + 1:]:
#         print(index, int(times[index]), prelim_basis, calc_next(int(times[index]), prelim_basis))
#         #     print()
#         # prod *= (index * calc_next(int(times[index]), prelim_basis))
#         new_times.append((index * prod * calc_next(int(times[index]), prelim_basis), int(times[index]) + 1))
#     offsets = offsets[1:]
#     print(offsets)
#     print(new_times)
# while not check_true(timestamp, times):
#     timestamp += calc_next(int(times[orders[1]]), prelim_basis)
    # for idx, index in enumerate(orders[1:]):
    #     # for sub_index in orders[idx + 1:]:
    #     print(index, int(times[index]), prelim_basis, calc_next(int(times[index]), prelim_basis))
    #     #     print()
    #     # prod *= (index * calc_next(int(times[index]), prelim_basis))
    #     new_times.append(index * calc_next(int(times[index]), prelim_basis))
# print(prod * prelim_basis)
# print(prod * prelim_basis)
# print(new_times)