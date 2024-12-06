instructions, details = open('input.txt','r').read().split("\n\n")
instructions = [[int(a) for a in ins.split("|")] for ins in instructions.split("\n")]
details = [[int(e) for e in d.split(",")] for d in details.split("\n")]

timeline : dict[int, list[int]] = {}
for ins in instructions:
    if ins[1] in timeline.keys():
        timeline[ins[1]].append(ins[0])
    else:
        timeline[ins[1]] = [ins[0]]

# ex: if we get timeline[53] we get all the numbers that CANNOT be after 53

def is_correct(detail : list[int], timeline: dict[int, list[int]]) -> bool:
    for i, page in enumerate(detail):
        try:
            if page in timeline.keys() and any([j in detail[i+1:] for j in timeline[page]]):
                return False
        except KeyError as k:
            print(timeline, '***', page, '**')
    return True

def get_middle_num(nums:list[int]) -> int:
    return nums[len(nums)//2]

correct = 0
middle_num_sum = 0

for detail in details:
    if is_correct(detail, timeline):
        correct += 1
        middle_num_sum += get_middle_num(detail)
        
        
print("Correct lines:", correct)
print(middle_num_sum)
