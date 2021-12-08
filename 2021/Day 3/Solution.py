from typing import List, Tuple

with open("input.txt", "r") as f:
    input_data = f.readlines()
    input_data = [i.strip("\n") for i in input_data]

sample_data = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]

def find_parameters(l:List[str]) -> Tuple[str]:
    result = []
    for n in range(len(l[0])):
        ones = sum(list(map(lambda x: x[n].count("1"), l)))
        zeros = sum(list(map(lambda x: x[n].count("0"), l)))
        if ones>zeros: result.append("1")
        else: result.append("0")
    gamma = "".join(result)
    epsilon = "".join(["1" if i=="0" else "0" for i in gamma])
    return gamma, epsilon

def calculate_power(l:List[str]) -> int:
    gamma = int(l[0],2)
    epsilon = int(l[1],2)
    power = gamma*epsilon
    return power

# Sample Input
sample_params = find_parameters(sample_data)
calculate_power(sample_params)

# Part 1 solution
input_params = find_parameters(input_data)
calculate_power(input_params)


def find_new_params(l:List[str]) -> Tuple[str]:
    oxygen_generator_rating = l.copy()
    co2_scrubber_rating = l.copy()

    for n in range(len(l[0])):
        oxygen_len = len(oxygen_generator_rating)
        co2_len = len(co2_scrubber_rating)

        ones_o = sum(list(map(lambda x: x[n].count("1"), oxygen_generator_rating)))
        zeros_o = sum(list(map(lambda x: x[n].count("0"), oxygen_generator_rating)))

        ones_c = sum(list(map(lambda x: x[n].count("1"), co2_scrubber_rating)))
        zeros_c = sum(list(map(lambda x: x[n].count("0"), co2_scrubber_rating)))
        if oxygen_len>1:
            if zeros_o>ones_o: oxygen_generator_rating = [i for i in oxygen_generator_rating if i[n]=="0"]
            else: oxygen_generator_rating = [i for i in oxygen_generator_rating if i[n]=="1"]
        else: continue
        if co2_len>1:
            if zeros_c>ones_c: co2_scrubber_rating = [i for i in co2_scrubber_rating if i[n]=="1"]
            else: co2_scrubber_rating = [i for i in co2_scrubber_rating if i[n]=="0"]
        else: continue
    return oxygen_generator_rating[0], co2_scrubber_rating[0]


# Sample data
sample_params2 = find_new_params(sample_data)
calculate_power(sample_params2)

# Input data
input_params2 = find_new_params(input_data)
calculate_power(input_params2)