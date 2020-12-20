from collections import defaultdict
input_file = open('Inputs/Input_4.txt', 'r')
req_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
curr_fields = set()
curr_valid_fields = set()
valid_by_fields = 0
validated = 0
heights = {'cm': (150, 193), 'in': (59, 76)}
eye_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
for row in input_file:
    row = row.strip('\n')
    # print(row)
    if not row:
        # print('break')
        # print(curr_fields)
        if curr_fields == req_fields:
            valid_by_fields += 1
        if curr_valid_fields == req_fields:
            validated += 1
        curr_fields = set()
        curr_valid_fields = set()
    else:
        fields = row.split(' ')
        for datum in fields:
            field, value = datum.split(':')
            if field != 'cid':
                if field == 'byr' and int(value) >= 1920 and int(value) <= 2002:
                    curr_valid_fields.add(field)
                elif field == 'iyr' and int(value) >= 2010 and int(value) <= 2020:
                    curr_valid_fields.add(field)
                elif field == 'eyr' and int(value) >= 2020 and int(value) <= 2030:
                    curr_valid_fields.add(field)
                elif field == 'hgt' and value[-2:] in heights:
                    # print(value)
                    height = int(value[:-2])
                    lo, hi = heights[value[-2:]]
                    if height >= lo and height <= hi:
                        curr_valid_fields.add(field)
                elif field == 'hcl' and value[0] == '#' and len(value) == 7:
                    try:
                        _ = int(value[1:], base=16)
                        curr_valid_fields.add(field)
                    except:
                        pass
                elif field == 'ecl' and value in eye_colors:
                    curr_valid_fields.add(field)
                elif field == 'pid' and len(value) == 9:
                    try:
                        _ = int(value)
                        curr_valid_fields.add(field)
                    except:
                        pass
                curr_fields.add(field)
print(valid_by_fields)
print(validated)
