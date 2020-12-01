
#squares = [x**2 for x in range(10)]

import itertools
mylist = range(10)

answers = []

with open('input_day1.txt', newline='') as file:
    lines = file.readlines()
    for a, b, c in itertools.combinations(lines, 3):
        if (int(a) + int(b) + int(c) == 2020):
            print(int(a)*int(b)*int(c))
