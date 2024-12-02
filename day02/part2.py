def is_safe(line: str) -> bool:
    nums = [int(r) for r in line.split()]
    is_inc = nums[1] - nums[0] > 0
    for i in range(1, len(nums)):
        dist = abs(nums[i] - nums[i-1])
        if (((nums[i] - nums[i-1]) > 0) != is_inc) or (dist < 1) or (dist > 3):
            return False
    return True      

def permute_safe(line: str):
    nums = [int(x) for x in line.split()]
    return any([is_safe(" ".join([str(a) for a in nums[0:i]+nums[i+1:]])) for i in range(len(nums))])
        
with open('input.txt','r') as file:
    lines = file.read().split("\n")
    counter = 0
    for line in lines:
        if is_safe(line):
            counter += 1
        elif permute_safe(line):
            counter += 1
    print(counter)