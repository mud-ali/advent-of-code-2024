from itertools import product as cwr

filename = "input.txt"
# filename = "test.txt"

def eval_expr(expr):
    a, op, b = expr.split(" ")
    if op == "+":
        return int(a) + int(b)
    elif op == "*":
        return int(a) * int(b)
    elif op == "|":
        return int(str(a) + str(b))

def eval_line(line):
    ops = line.split(" ")
    total = eval_expr(" ".join(ops[0:3]))
    for i in range(3, len(ops), 2):
        a = total
        b = int(ops[i+1])
        total = eval_expr(str(a) + " " + ops[i] + " " + str(b))
    return total
        
        

def possible_line(line):
    ans, args = line.strip().split(": ")
    args = " + ".join(args.split(" "))
    ans = int(ans)
    if eval_line(args) == ans:
        return ans
    args = args.replace(" + ", " ")
    options = list(cwr("+*|", repeat=args.count(" ")))
    for option in options:
        new_args = args
        for o in option:
            new_args = new_args.replace(" ", o, 1)
        new_args = new_args.replace("+", " + ").replace("*", " * ").replace("|", " | ")
        if eval_line(new_args) == ans:
            return ans
    
    return 0
    

with open(filename, "r") as file:
    lines = file.readlines()
    count = 0
    for line in lines:
        count += possible_line(line)
    print(count)

assert eval_line("1 + 2 * 3 + 4 * 5 + 6") == 71
assert eval_line("10 * 19") == 190
assert eval_line("10 + 19") == 29
assert eval_line("81 + 40 * 27") == 3267
assert eval_line("81 * 40 + 27") == 3267
assert eval_line("11 + 6 * 16 + 20") == 292
