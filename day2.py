

def split_number(numbers):
    arrnum = numbers.split("-")
    return arrnum

def poscontains(position, string, char):
    if char == string[int(position)]:
        return True
    else:
        return False

def apply_rules(pos1, pos2):
    if pos1 is True and pos2 is False:
        return True
    if pos1 is False and pos2 is True:
        return True
    if pos1 is True and pos2 is True:
        return False
    if pos1 is False and pos2 is False:
        return False
    else:
        return False

def valid_password(positions, string, char):
    if apply_rules(poscontains(positions[0], string, char), poscontains(positions[1], string, char)):
        return True

with open('input_day2.txt', newline='') as file:
    lines = file.readlines()
    validpassword = []
    for line in lines:
        split = line.split(":")
        rules = split[0].split(" ")
        numbers = rules[0]
        letter = rules[1]
        count = int(split[1].count(letter))
        highlow = split_number(numbers)
        #if (count <= int(highlow[1])) & (count >= int(highlow[0])):
        #    print(count)
        #    validpassword.append(split[1])

        if valid_password(highlow, split[1], letter):
            validpassword.append(split[1])

print(len(validpassword))
