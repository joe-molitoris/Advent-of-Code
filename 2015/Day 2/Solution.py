from typing import List

with open("input.txt", "r") as f:
    data = f.read().splitlines()

def parse_data(data:List[str]) -> List[str]:
    return [[int(x) for x in i.split("x")] for i in data]

clean_data = parse_data(data)

def wrapping_paper_needed(data:List[List[int]]) -> List[int]:
    length = [i[0] for i in clean_data]
    width = [i[1] for i in clean_data]
    height = [i[2] for i in clean_data]
    return sum([((2*l*w) + (2*w*h) + (2*h*l))+min([l*w,h*w,h*l]) for l,h,w in zip(length, width, height)])

# Solution pt. 1
wrapping_paper_needed(clean_data)

