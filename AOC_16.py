from collections import defaultdict
import string, re
from math import cos, sin, pi
input_file = open('Inputs/Input_16.txt', 'r')
# print(input_file.read().strip('\n').split('\n\n'))
info, my_ticket, tickets = input_file.read().strip('\n').split('\n\n')
fields = {}
for field in info.split('\n'):
    # print(field)
    name, vals = field.split(': ')
    fields[name] = set()
    for val in vals.split(' or '):
        lo, hi = val.split('-')
        for i in range(int(lo), int(hi) + 1):
            fields[name].add(i)
my_ticket = my_ticket.split('\n')[-1].split(',')
# print(ticket)
nearby_tickets = tickets.split('\n')[1:]
error = 0
tickets = []
valid_tickets = set()
for idx, ticket in enumerate(nearby_tickets):
    tickets.append([int(val) for val in ticket.split(',')])
    valid_tickets.add(idx)
invalid_tickets = set()
for idx, ticket in enumerate(tickets):
    for val in ticket:
        is_valid = False
        for values in fields.values():
            if val in values:
                is_valid = True
                break
        if not is_valid:
            invalid_tickets.add(idx)
            error += val
print(error)
valid_tickets = valid_tickets.difference(invalid_tickets)
poss_fields = [set(fields.keys()) for _ in fields.keys()]
for tick_id in valid_tickets:
    for idx, val in enumerate(tickets[tick_id]):
        for field, values in fields.items():
            if val not in values:
                poss_fields[idx].remove(field)
going = True
while going:
    going = False
    for idx, poss_field_set in enumerate(poss_fields):
        if len(poss_field_set) > 1:
            going = True
        else:
            val = list(poss_field_set)[0]
            for s_idx, inner_set in enumerate(poss_fields):
                if s_idx != idx:
                    inner_set.discard(val)
tot = 1
for field, val in zip(poss_fields, my_ticket):
    field = list(field)[0]
    # print(field)
    if field.startswith('departure'):
        tot *= int(val)
print(tot)
# print(poss_fields)