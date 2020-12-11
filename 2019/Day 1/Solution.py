from typing import List

with open("input.txt", "r") as f:
    data = f.read().splitlines()
data = [int(i) for i in data]

def fuel_calculation(mass:int) -> int:
    return (mass//3)-2

def total_fuel_requirement(data:List[int]) -> int:
    return sum([fuel_calculation(i) for i in data])

def new_fuel_requirement(data:List[int]) -> int:
    result = []
    for i in range(len(data)):
        fuel = fuel_calculation(data[i])
        total_fuel = fuel
        while fuel>0:
            fuel = fuel_calculation(fuel)
            total_fuel += fuel
        result.append(total_fuel)
    return sum(result)


# Solution pt. 1
total_fuel_requirement(data)

# Solution pt. 2
new_fuel_requirement(data)

