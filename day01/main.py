filename = "input.txt"
# filename = "test.txt"

with open(filename, 'r') as file:
    lines = file.read().split('\n')
    a = []
    b = []
    for line in lines:
        x,y = line.split()
        a.append(x)
        b.append(y)
    a.sort()
    b.sort()
    
    # part 1
    dist = 0
    for i in range(len(a)):
        dist += abs(int(a[i])-int(b[i]))
    print(dist)
    
    # part 2
    score = 0
    for item in a:
        score += b.count(item) * int(item)
    print(score)