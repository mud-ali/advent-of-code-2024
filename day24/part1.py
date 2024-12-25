filename = 'input.txt'
# comment out to run on real input
# filename = 'test.txt'


with open(filename, 'r') as file:
    given, equations = [a.split("\n") for a in file.read().split("\n\n")]
    
    known = {}
    for g in given:
        key, value = g.split(": ")
        known[key] = int(value)
    
    i = 0
    while len(equations) > 0:
        equation = equations[i].replace("-> ", '').split()
        # print(equation)
        if equation[0] in known.keys() and equation[2] in known.keys():
            ans = None
            op1 = known[equation[0]]
            op2 = known[equation[2]]
            match equation[1]:
                case 'AND':
                    ans = op1 & op2
                case 'OR':
                    ans = op1 | op2
                case 'XOR':
                    ans = op1 ^ op2 
            known[equation[3]] = ans
            equations.pop(i)
            # print(equation, "======", ans)
        else:
            print(equation[0], "\t", equation[2], "\t", known.keys())
        
        if len(equations) > 0:
            i = (i + 1) % len(equations)
    
total_bin = ''
z=0
while True:
    key = 'z' + str(z).zfill(2)
    if key in known.keys():
       total_bin += str(known[key])
    else: break
   
    z+=1 

total_bin = total_bin[::-1]

print(total_bin)
print(int(total_bin, 2))