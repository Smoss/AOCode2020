from collections import defaultdict
import string, re
from math import cos, sin, pi
from operator import add, mul
input_file = open('Inputs/Input_18.txt', 'r')
tot = 0
opps = {'+': add, '*': mul}
def eval_new_math(expr, depth):
    next_exec = ''
    opp = ''
    curr_val = None
    while expr:
        nxt = expr.pop(0)
        # print('stack', nxt, curr_val)
        # print(next_exec)
        if nxt == '(':
            nxt = str(eval_new_math(expr, depth + 1))
            # print('ret', nxt, curr_val, opp)
        if nxt == ')':
            if opp == '+':
                # ret_flag = False
                curr_val = opps[opp](curr_val, int(nxt))
                opp = ''
                next_exec += str(curr_val)
            elif opp == '*':
                next_exec += '{} {} {}'.format(curr_val, opp, nxt)
                curr_val = ''
            curr_val = eval(next_exec + str(curr_val))
            return curr_val
        if opp == '+':
            # ret_flag = False
            curr_val = opps[opp](curr_val, int(nxt))
            opp = ''
        elif opp == '*':
            next_exec += '{} {} '.format(curr_val, opp)
            curr_val = int(nxt)
            opp = ''
        elif curr_val is None:
            curr_val = int(nxt)
        else:
            opp = nxt
    curr_val = eval(next_exec + str(curr_val))
    return curr_val

tot = 0
for line in input_file:
    line = line.strip('\n').replace('(', '( ').replace(')', ' )').split(' ')
    val = eval_new_math(line, 0)
    print(val)
    tot += val
    # print(line)
print(tot)

