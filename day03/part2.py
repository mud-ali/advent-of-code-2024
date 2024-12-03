import re

input_text = "input.txt"

badpattern = 'don\'t\(\)|mul\(\d*,\d*\)|do\(\)'
total = 0

with open(input_text) as f:
    lines = f.readlines()
    do = True
    for line in lines:
        result = [a for a in re.findall(badpattern, line) if a != '']
        for r in result:
            if r=='do()':
                do = True
            elif r=='don\'t()':
                do = False
            elif do and re.sub('mul\(\d*,\d*\)', '', r)=='':
                a,b = list(map(int, re.findall('mul\((\d*,\d*)\)', r)[0].split(",")))
                total += a*b

print(total)