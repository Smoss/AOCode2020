input_file = open('Inputs/Input_1.txt', 'r')
vals = [int(val) for val in input_file]
for idx, val_1 in enumerate(vals):
    for val_2 in vals[idx + 1:]:
        if val_1 + val_2 == 2020:
            print(val_1 * val_2)
            break
for idx, val_1 in enumerate(vals):
    for idx_2, val_2 in enumerate(vals[idx + 1:]):
        for val_3 in vals[idx_2 + idx + 1:]:
            if val_1 + val_2 + val_3 == 2020:
                print(val_1 * val_2 *val_3)
                break