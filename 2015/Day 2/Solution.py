from typing import List

with open("input.txt", "r") as f:
    data = f.read().splitlines()

def parse_data(data:List[str]) -> List[str]:
    return [[int(x) for x in i.split("x")] for i in data]

clean_data = parse_data(data)

def wrapping_paper_needed(data:List[List[int]]) -> int:
    length = [i[0] for i in clean_data]
    width = [i[1] for i in clean_data]
    height = [i[2] for i in clean_data]
    return sum([((2*l*w) + (2*w*h) + (2*h*l))+min([l*w,h*w,h*l]) for l,h,w in zip(length, width, height)])

def ribbon_needed(data:List[List[int]]) -> int:
    sorted_data = [sorted([i for i in e]) for e in data]
    result = [i[0]*2+i[1]*2+(i[0]*i[1]*i[2]) for i in sorted_data]
    return sum(result)

# Solution pt. 1
wrapping_paper_needed(clean_data)

# Solution pt. 2
ribbon_needed(clean_data)

