from typing import List
import re

with open("input.txt") as f:
    rules = f.read().splitlines()


def find_num_bags(rules:List[str]) -> int:
    '''
    Find total number of bag types that can contain "shiny gold" bags.
    This includes bags that may be nested in other bags.
    '''
    # Identify location of "contain" to parse string into dict
    contain_loc = [i.find(" contain ") for i in rules]
    contain_len = len(" contain ")
    rules_dict = {rules[n][:contain_loc[n]]: rules[n][contain_loc[n]+contain_len:] for n in range(len(rules))}

    # Set s to True in order to run while loop
    s=True
    # last_set defined as names of any dictionary items that include 'shiny gold'
    last_set = set([i for i in rules_dict if "shiny gold" in rules_dict[i]])
    # This list will contain all values that are encountered during the while loop
    # i.e. all bags that held a bag in which 'shiny gold' was in.
    total_list = list(last_set)
    # This loop will go through each level of bags and add to the list of total bags
    # any bags that each item was included in.
    # Sets are taken to remove duplicate bags.
    while s:
        next_set = set([i for i in rules_dict for b in last_set if b.strip(" bags") in rules_dict[i]])
        last_set = next_set
        total_list += list(next_set)
        if len(next_set)==0:
            s=False
    return len(set(total_list))

def count_bags(rules:List[str]) -> int:
    '''
    Based on bag rules, count number of bags nested within a shiny gold bag.
    '''
    # Identify location of "contain" to parse string into dict
    contain_loc = [i.find(" contain ") for i in rules]
    contain_len = len(" contain ")
    rules_dict = {rules[n][:contain_loc[n]].replace(" bags", ""): rules[n][contain_loc[n]+contain_len:].split(",") for n in range(len(rules))}

    # Creates a nested dict with numbers of bags and colors
    for i in rules_dict:
        for n in range(len(rules_dict[i])):
            for x in [",", ".", "bag", "bags", " "]:
                rules_dict[i][n] = rules_dict[i][n].strip(x)
    number_rules = {k:{key:val for key,val in zip([rules_dict[k][n][2:] for n in range(len(rules_dict[k]))],[int(x) for i in rules_dict[k] for x in i.split() if x.isdigit()])} for k in rules_dict}

    # Starts out by identifying bags in a shiny gold bag
    last_bags = [i for i in number_rules['shiny gold'].items()]
    # creates a total list that will eventually have all the bag colors and numbers
    total_list = last_bags
    # Set s to True for while loop
    s = True
    # For each bag contained in previous level, creates a tuple of bags within THAT bag
    # and multiplies the number of occurences of the parent bag by the number of occurences
    # of the index bag. Loop terminates when there are no more bags nested in a parent level.
    while s:
        next_bags = [(k, v*b[1]) for b in last_bags for k,v in zip(number_rules[b[0]].keys(), number_rules[b[0]].values())]
        last_bags = next_bags
        total_list += next_bags
        if len(next_bags)==0:
            s=False
    return sum([i[1] for i in total_list])

# Solution pt. 1
find_num_bags(rules)

# Solution pt. 2
count_bags(rules)




