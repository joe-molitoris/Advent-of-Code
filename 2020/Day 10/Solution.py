from typing import List
from collections import defaultdict

with open("input.txt") as f:
    data = f.read().splitlines()

data = [int(i) for i in data]

def clean_and_setup(data:List[int]) -> int:
    new_data = [0]+sorted(data)
    new_data.append(new_data[-1]+3)
    return new_data

def get_diffs(data:List[int]) -> List[int]:
    result = [data[i]-data[i-1] for i in range(1, len(data))]
    return result

def sum_differences(data:List[int]) -> int:
    data = clean_and_setup(data)
    difference = get_diffs(data)
    threes = difference.count(3)
    ones = difference.count(1)
    return threes*ones

def find_arrangements(data:List[int]) -> int:
    data = clean_and_setup(data)
    ways = defaultdict(int)
    ways[0]=1
    for i in data[1:]:
        ways[i] = ways[i-1]+ways[i-2]+ways[i-3]
    return max(ways.values())

# Solution pt. 1
sum_differences(data)

# Solution pt. 2
find_arrangements(data)