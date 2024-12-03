import re

input_text = "input.txt"
# input_text = "test.txt"

pattern = 'mul\((\d*,\d*)\)'
total = 0

with open(input_text) as f:
    lines = f.readlines()
    for line in lines:
        result = re.findall(pattern, line)
        print(result)
        for r in result:
            a,b =[int(j) for j in r.split(",")]
            total += a * b

print(total)