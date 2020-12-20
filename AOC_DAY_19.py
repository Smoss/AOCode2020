from collections import defaultdict
import string, re
from math import cos, sin, pi
from operator import add, mul
input_file = open('Inputs/Input_19.txt', 'r')
rules, words = input_file.read().split('\n\n')
rule_dict = {}
rules_to_update = []
# print(rules)
updated_rules = set()
str_rules = set()
for rule in rules.split('\n'):
    id, rule = rule.split(': ')
    # print(id,rule)
    if '"' in rule:
        str_rules.add(id)
        updated_rules.add(id)
        rule = rule.strip('"')
        # print(rule)
    else:
        rules_to_update.append(id)
    rule_dict[id] = rule

# def recursively_update(rule_id, depth):
#     if rule_id in updated_rules:
#         return
#     updated_rules.add(rule_id)
#     rule = rule_dict[rule_id]
#     needed_rules = rule.replace('| ', '').split(' ')
#     # print(needed_rules, rule_id, depth)
#     for needed_rule_id in set(needed_rules):
#         # print(needed_rule_id, updated_rules)
#         if needed_rule_id in updated_rules or not needed_rule_id in rule_dict:
#             # print('fuck')>??
#             continue
#         recursively_update(needed_rule_id, depth + 1)
#     rule_list = rule.split(' | ')
#     final_rules = []
#     # print(rule_list, rule_id)
#     for rule in rule_list:
#         final_rules.append([comp for comp in rule.split(' ')])
#     # final_rule = ' and '.join(final_rules)
#     rule_dict[rule_id] = final_rules

# for rule_id in rules_to_update:
#     # print(updated_rules)
#     recursively_update(rule_id, 0)
def check_rule(rule_id, indexes, word):
    # passed = True
    rule = rule_dict[rule_id]
    # print(indexes, rule_id)
    indexes = {index for index in indexes if index < len(word)}
    if not indexes:
        return set()
    if rule_id in str_rules:
        valids = {index + 1 for index in indexes if word[index] == rule}
        return valids
    paths = rule.split(' | ')
    counters = None
    passed = True
    ways_out = set()
    for path in paths:
        counters = set(list(indexes)[:])
        # print(rule_id, counters, ':',  path)
        rules = path.split(' ')
        for sub_rule_id in rules:
            # print(rule_id, index, ':',  sub_rule_id)
            counters = check_rule(sub_rule_id, counters, word)
            # counter = addr
            # print(counters)
        ways_out = ways_out.union(counters)
    return ways_out
# print(rule_dict['11'],':',  rule_dict['8'])
tot = 0
for string_match in words.split('\n'):
    passed = 1
    counters = check_rule('0', {0}, string_match)
    # print(string_match, counters, len(string_match))
    if len(string_match) in counters:
        tot += passed
print(tot)