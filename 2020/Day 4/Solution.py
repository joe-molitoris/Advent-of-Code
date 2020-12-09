with open("input.txt", "r") as f:
    data = f.read()

def clean_data(data:str)  -> dict:
    '''
    Makes data more user friendly
    '''
    records = data.split("\n\n")
    cleaned_data = [i.replace("\n", " ").split() for i in records]
    dictionary_records = [{i.split(":")[0]:i.split(":")[1] for i in cleaned_data[n]} for n in range(len(cleaned_data))]
    return dictionary_records

def count_valid_passports(data:dict)  -> int:
    '''
    Counts number of passsports that include required fields. CID is not required.
    '''
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    result = []
    for n in range(len(data)):
        result.append(all([True if i in set(data[n].keys()) else False for i in required_fields[:-1]]))
    return sum(result)

def count_valid_passports_new_rules(data:dict) -> int:
    '''
    Counts number of passsports that include required fields. CID is not required.
    '''
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    result = []
    for n in range(len(data)):
        if not all([True if i in set(data[n].keys()) else False for i in required_fields[:-1]]):
            result.append(False)
        else:
            byr = (2002>=int(data[n]['byr'])>=1920) & (len(data[n]['byr'])==4)
            iyr = (2020>=int(data[n]['iyr'])>=2010) & (len(data[n]['iyr'])==4)
            eyr = (2030>=int(data[n]['eyr'])>=2020) & (len(data[n]['eyr'])==4)
            if (data[n]['hgt'].endswith("in")) | (data[n]['hgt'].endswith("cm")):
                hgt = ((76>=int(data[n]['hgt'][:-2])>=59) & (data[n]['hgt'].endswith("in"))) | ((193>=int(data[n]['hgt'][:-2])>=150) & (data[n]['hgt'].endswith("cm")))
            else:
                hgt = False
            hcl = ((data[n]['hcl'][0].startswith("#")) & (all([True if (i in [str(i) for i in range(0,10)]) or (i in ['a', 'b', 'c', 'd', 'e', 'f']) else False for i in data[n]['hcl'][1:]])))
            ecl = data[n]['ecl'] in ["amb", 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            pid = (len(data[n]['pid'])==9) & (all([i.isnumeric() for i in data[n]['pid']]))
            result.append(all([byr, iyr, eyr, hgt, hcl, ecl, pid]))
    return sum(result)

data = clean_data(data)

# Solution pt. 1
count_valid_passports(data)

# Solution pt. 2
count_valid_passports_new_rules(data)

