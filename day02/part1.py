def is_safe(line: str) -> bool:
    nums = [int(r) for r in line.split()]
    is_inc : bool = nums[1] - nums[0] > 0
    for i in range(1, len(nums)):
        dist = abs(nums[i] - nums[i-1])
        if (((nums[i] - nums[i-1]) > 0) != is_inc) or (dist < 1) or (dist > 3):
            return False
    return True
            

with open('input.txt','r') as file:
    lines = file.read().split("\n")
    counter = 0
    for line in lines:
        if is_safe(line):
            counter += 1
    
    print(counter)