import itertools
from itertools import combinations

def check_ends(list):
    if list[0] > 3:
        return False
    else:
        return True

def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            print(item)
            yield [seq[0]]+item
            yield item

with open('input_test10.txt', newline='') as file:
    lines = file.readlines()

    ints = []

    for line in lines:
        ints.append(int(line.strip()))

    ints.sort()
    print(ints)
    diffs =  [j - i for i, j in zip(ints[:-1], ints[1:])]
    print(diffs)
    ones = diffs.count(1)
    ones = ones + 1
    threes = diffs.count(3)
    threes = threes + 1
    print(ones, threes)
    print(ones * threes)

    valid = 0
    items = powerset(ints)
    count_ones = 0
    for x in range(0, len(diffs)-1):
        if diffs[x] == 1 and diffs[x+1] == 1:
            print(diffs[x])
            count_ones = count_ones + 1


    print(count_ones)

