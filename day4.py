import re

fields = ['byr', 'eyr', 'iyr', 'hcl', 'ecl', 'hgt', 'pid', 'cid']

def birth_year(year):
    if 1920 <= year <= 2002:
        return True
    else:
        return False

def issue_year(year):
    if 2010 <= year <= 2020:
        return True
    else:
        return False

def exp_year(year):
    if 2020 <= year <= 2030:
        return True
    else:
        return False

def height_check(height):
    if 'cm' in height:
        value = int(height.replace("cm", ""))
        if 150 <= value <= 193:
            return True
        else:
            return False
    elif 'in' in height:
        value = int(height.replace("in", ""))
        if 59 <= value <= 76:
            return True
        else:
            return False
    else:
        return False

def hair_colour(colour):
    hc = re.compile('#[a-f,0-9,A-F][a-f,0-9,A-F][a-f,0-9,A-F][a-f,0-9,A-F][a-f,0-9,A-F][a-f,0-9,A-F]')
    if hc.match(colour) is not None:
        return True
    else:
        return False

def eye_colour(colour):
    ec = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if colour in ec:
        return True
    else:
        return False

def passport_valid(passport):
    pv = re.compile('\d{9}')

    if len(passport) != 9:
        return False
    if pv.match(passport) is not None:
        return True
    else:
        return False

with open('input4.txt', newline='\n') as file:
    lines = file.readlines()
    entries = []
    valid_list = []
    curr_entry = ""
    valid_entries = 0
    invalid = 0

    for line in lines:
        entry = ""
        if line.strip() == "":
            entries.append(curr_entry)
            curr_entry = ""
        else:
            curr_entry = curr_entry + " " + line.strip()

    for entry in entries:
        entry_fields = entry.split(" ")[1:]
        present = []
        key_values = {}
        for field_s in entry_fields:
            f = field_s.split(":")[0]
            present.append(str(f))
            key_values[str(f)] = field_s.split(":")[1]

        intersection = set(present).intersection(fields)
        if len(intersection) == 8:
            valid_list.append(key_values)
        elif len(intersection) == 7:
            if ('cid' in intersection):
                invalid = invalid + 1
            else:
                valid_list.append(key_values)
        else:
            invalid = invalid + 1

    invalid = 0
    for entry in valid_list:
        checks = []
        checks.append(birth_year(int(entry['byr'])))
        checks.append(issue_year(int(entry['iyr'])))
        checks.append(exp_year(int(entry['eyr'])))
        checks.append(height_check(entry['hgt']))
        checks.append(eye_colour(entry['ecl']))
        checks.append(hair_colour(entry['hcl']))
        checks.append(passport_valid(entry['pid']))
        if False in checks:
            invalid = invalid + 1
        else:
            valid_entries = valid_entries + 1

    print(valid_entries)
    print(valid_entries + invalid)

