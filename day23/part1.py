filename = 'input.txt'
# comment out to run on real input
filename = 'test.txt'


with open(filename, 'r') as file:
    lines = file.read().split("\n")
    conns = {}
    
    for line in lines:
        c1,c2 = line.split("-")
        if c1 not in conns.keys():
            conns[c1] = [c2]
        else:
            conns[c1].append(c2)
        
        if c2 not in conns.keys():
            conns[c2] = [c1]
        else:
            conns[c2].append(c1)
    
    # print(conns, "\n\n")
    
    games = []
    for c in conns.keys():
        degree_one = conns[c]
        for c1 in degree_one:
            deg_two = conns[c1]
            for c2 in deg_two:
                deg_three = conns[c2]
                for c3 in deg_three:
                    if c3==c:
                        games.append(",".join(sorted([c,c1,c2])))
                    
    games = sorted(list(set(games)))
    print(len(games))
    
    total = 0
    for game in games:
        if any(g[0]=="t" for g in game.split(",")):
            total += 1
            
    print(total)
            
    
