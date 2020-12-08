
with open('input_day3.txt', newline='') as file:
    lines = file.readlines()[::2]
    index = 0
    count_trees = 0

    for line in lines:
        line = line.strip()
        print(index, line[index])
        if line[index] == '#':
            count_trees = count_trees + 1
            print(count_trees)
        index = index + 1

        if index >= len(line):
          index = index - len(line)


    print(count_trees)
