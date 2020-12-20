from collections import defaultdict
import string, re
from math import cos, sin, pi
input_file = open('Inputs/Input_14.txt', 'r')
mask = 'X' * 36
addrs = {}
for line in input_file:
    if line.startswith('mask'):
        mask = line.split(' = ')[1].strip('\n')
        continue
    mem, val = line.strip('\n').split(' = ')
    val = int(val)
    val = bin(val)[2:]
    # print(val)
    mem_val = list(val.zfill(36))
    # print('###')
    # print(mask)
    # print(''.join(mem_val))
    # for idx, char in enumerate(mask):
    #     if char in ['0', '1']:
    #         mem_val[idx] = char
    mem_val = ''.join(mem_val)
    # print(mem_val)
    # pattern = re.compile(r'\d+')
    # address = pattern.match(mem)
    address = mem[mem.find('[') + 1: mem.find(']')]
    address = list(bin(int(address))[2:].zfill(36))
    for idx, char in enumerate(mask):
        if char in ['1', 'X']:
            address[idx] = char
    # print(''.join(address))
    # print(mem, addresss)
    addresses = [[]]
    if not 'X' in address:
        addresses = [address]
    else:
        for idx, char in enumerate(address):
            if char !='X':
                for addr in addresses:
                    addr.append(char)
            else:
                new_addresses = []
                for i in range(len(addresses)):
                    new_addresses.append(addresses[i][:])
                    addresses[i].append('1')
                    new_addresses[i].append('0')
                addresses += new_addresses
                # print(len(addresses))
    # print(len(addresses))
    for addr in addresses:
        addrs[''.join(addr)] = mem_val
# print(addrs)
tot = 0
for key, val in addrs.items():
    # print(int(val, base=2))
    tot += int(val, base=2)
print(tot)