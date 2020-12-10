with open("input.txt", "r") as f:
    data = f.read().splitlines()

def find_nice_strings(data:str)->int:
    vowels = ["a","e","i","o","u"]
    forbidden = ["ab", "cd", "pq", "xy"]
    meets_requirements=[]
    for i in data:
        all_met = [False]
        # At least three vowels in string
        included_vowels = [i.count(v) for v in vowels if v in i]
        if sum(included_vowels)>=3:
            all_met[-1] = True
        # Forbidden not in string
        all_met.append(True)
        for f in forbidden:
            if f in i:
                all_met[-1] = False
                break
        # A double letter occurs
        all_met.append(False)
        for l in set(i):
            if l*2 in i:
                all_met[-1] = True
                break
        meets_requirements.append(all_met)
    return sum([all(m) for m in meets_requirements])

def new_rules(data:str) -> int:
    

# Solution pt. 1
find_nice_strings(data)

# Solution pt. 2
