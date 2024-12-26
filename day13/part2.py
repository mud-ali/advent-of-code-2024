import numpy as np

filename = 'input.txt'
# comment out to run on real input
# filename = 'test.txt'

total = 0

with open(filename, 'r') as file:
    games = file.read().split("\n\n")
    for game in games:
        
        p,q,g = [[int(a[2:]) for a in g[g.index(":")+2:].split(", ")] for g in game.split("\n")]
        goal = np.array([gi + 10000000000000 for gi in g])
        matrix = np.array([[p[0],q[0]],[p[1],q[1]]])
        A,B = np.linalg.solve(matrix, goal)
        # print(matrix,goal)
        
        if round(A, 4) == int(round(A, 4)) and round(B,4) == int(round(B, 4)):
            tokens = (3*A) + B
            # print(tokens)
            total += tokens
        else:
            # print(A, int(A), B, int(B))
            pass
    

print(total)