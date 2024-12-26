filename = 'input.txt'
# comment out to run on real input
# filename = 'test.txt'

total = 0

def prune(n:int) -> int:
    return n % 16777216

def mix(a,b) -> int:
    return a ^ b


def new_secret_num(secret_num:int) -> int:
    n = secret_num
    for i in range(2000):
        n = prune(mix(n, n*64))
        n = prune(mix(n, n//32))
        n = prune(mix(n, n*2048))
    return n

with open(filename, 'r') as file:
    lines = [int(a) for a in file.read().split("\n")]
    for line in lines:
        total+= new_secret_num(line)
    

print(total)