import re

def get_last_num(disk_expanded : list[str]) -> int:
    return int([a for a in disk_expanded if a != '.' ][-1])

def has_gap(disk_state: list[str]) -> bool:
    seenDot = False
    for block in disk_state:
        if block=='.':
            seenDot = True
        elif seenDot:
            return True
    
    return False

def swap(arr : list[str], last_item : str, first_item : str):
    i_0 = arr.index(first_item)
    i_f = max(i for i, val in enumerate(arr) if val == last_item)
    
    arr[i_0] = last_item
    arr[i_f] = first_item

def checksum(arr:list[str]) -> int:
    total = 0
    for i, item in enumerate(arr):
        if item == '.': break
        total += i * int(item)
    return total

filename = 'input.txt'
# comment out to run on real input
filename = 'test.txt'

total = 0

file = open(filename, 'r')

disk_map = [int(a) for a in list(file.read())]
file.close()

disk = []

isFree = False
next_num = 0
for i in range(len(disk_map)):
    if isFree:
        for _ in range(disk_map[i]):
            disk.append('.')
    else:
        for _ in range(disk_map[i]):
            disk.append(str(next_num))
        next_num += 1
    isFree = not isFree

print(disk)

while has_gap(disk):
    swap(disk, str(get_last_num(disk)), '.')
    # print(''.join(disk))


print(checksum(disk))