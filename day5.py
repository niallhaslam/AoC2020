
def binary(string):
    bit = ""
    for char in string:
        if char == 'F':
            bit = bit + "0"
        else:
            bit = bit + "1"
    return bit

def columns(string):
    bit = ""
    for char in string:
        if char == 'L':
            bit = bit + "0"
        else:
            bit = bit + "1"
    return bit

def get_seat(row, cols):
    value = row * 8
    value = value + cols
    return value

with open('input5.txt', newline='\n') as file:
    lines = file.readlines()

    values = []
    value = 0
    for line in lines:
        row = line[0:7]
        column = line.strip()[-3:]

        bits = binary(row)
        ints = int(bits, 2)
        cols = columns(column)
        cols_int = int(cols, 2)

        seat = get_seat(ints, cols_int)
        values.append(int(seat))
        if seat > value:
            value = seat

    values = sorted(values)
    pot_values = [*range(84,901)]
    print(pot_values)
    print(values)
    print(value)
