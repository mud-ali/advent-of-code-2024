import numpy as np

filename = 'input.txt'
# comment out to run on real input
# filename = 'test.txt'

total = 0

locks = []
keys = []

with open(filename, 'r') as file:
    items = [[list(e) for e in data.split("\n")] for data in file.read().split("\n\n")]
    for item in items:
        if all(cell=="#" for cell in item[0]):
            counting = '#'
        else: counting = '.'
        heights = ["".join(row).count(counting) for row in np.transpose(np.array(item[1:])).tolist()]

        if counting == "#":
            locks.append(heights)
        else:
            keys.append([5-h for h in heights])
            
for lock in locks:
    for key in keys:
        try:
            for i in range(len(key)):
                if key[i]+lock[i] > 5:
                    raise KeyError
            total += 1
        except KeyError as err:
            continue

print(total)

    
