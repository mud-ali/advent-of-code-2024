filename = 'input.txt'

GRID_HEIGHT = 103
GRID_WIDTH = 101

if filename == 'test.txt':
    GRID_HEIGHT = 7
    GRID_WIDTH = 11

pos=[]
vels=[]
with open(filename, 'r') as file:
    lines = [[[int(a) for a in d.split("=")[1].split(",")] for d in datapoint.split()] for datapoint in file.read().split("\n")]
    for line in lines:
        pos.append(line[0])
        vels.append(line[1])

def print_grid():
    global pos
    grid = [['0'for __ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for p in pos:
        grid[p[1]][p[0]] = str(int(grid[p[1]][p[0]])+1)
    for row in grid:
        print("".join(row).replace("0","."))


for iter in range(1,1000000000):
    for i in range(len(pos)):
        pos[i][0] += vels[i][0]
        pos[i][0] %= GRID_WIDTH
        
        pos[i][1] += vels[i][1]
        pos[i][1] %= GRID_HEIGHT
    
    if len(pos) == len(set(["".join([str(s) for s in a]) for a in pos])):
        print(iter)
        print()
        print_grid()
        print("\n\n")
        break