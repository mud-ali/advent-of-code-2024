filename = 'input.txt'
# comment out to run on real input
# filename = 'test.txt'

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


# print(pos, vels)

for i in range(len(pos)):
    pos[i][0] += (vels[i][0] * 100)
    pos[i][0] %= GRID_WIDTH
    
    pos[i][1] += (vels[i][1] * 100)
    pos[i][1] %= GRID_HEIGHT
    
    
quadrants = [0,0,0,0]

for p in pos:
    if 0 <= p[0] < (GRID_WIDTH // 2): # on the left
        if 0 <= p[1] < (GRID_HEIGHT // 2): # top left
            quadrants[0] += 1
        elif p[1] != GRID_HEIGHT // 2:
            quadrants[2] += 1
    elif p[0] != GRID_WIDTH // 2:
        if 0 <= p[1] < (GRID_HEIGHT // 2): # top right
            quadrants[1] += 1
        elif p[1] != GRID_HEIGHT // 2:
            quadrants[3] += 1
            
print(quadrants)

product = 1
for q in quadrants:
    product *= q
    
print(f'Safety factor = \n{product}')