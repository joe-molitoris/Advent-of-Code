from typing import List
with open("input.txt", "r") as f:
    data = f.read().splitlines()

data = [int(i) for i in data]

def search_preamble(data:List[int], pream_length:int=25) -> bool:
    target = data[pream_length]
    preamble = data[:pream_length]
    components = [target-i for i in preamble]
    if [c for c in components if c in preamble]:
        return True
    return False

def first_invalid(data:List[int], pream_length:int=25) -> int:
    for i in range(0, len(data)-pream_length+1):
        result = search_preamble(data[i:pream_length+1+i], pream_length=pream_length)
        if result==False:
            return data[pream_length+i]

def find_contiguous(data:List[int]) -> int:
    terminal_value = first_invalid(data)
    terminal_ix = data.index(terminal_value)
    contig = {sum(data[i:i+n]):data[i:i+n] for n in range(1,terminal_ix) for i in range(terminal_ix)}
    return min(contig[terminal_value]) + max(contig[terminal_value])

# Solution pt. 1
first_invalid(data)

# Solution pt. 2
find_contiguous(data)


