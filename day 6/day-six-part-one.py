import math


def solve_day_six_part_one():
    f = open("inputs/day-six-input.txt", "r")

    columns = []
    firstLine = True

    for line in f:
        line = line.strip()
        rowNums = line.split()
        if firstLine:
            for num in rowNums:
                columns.append([int(num)])
            firstLine = False
        else:
            for i in range(len(rowNums)):
                if rowNums[1] == '+' or rowNums[1] == '*':
                    columns[i].append(rowNums[i])
                else:
                    columns[i].append(int(rowNums[i]))

    totalResults = 0
    for i in range(len(columns)):
        col = columns[i]
        operator = col.pop()

        if operator == '+':
            totalResults += sum(col)
        elif operator == '*':
            totalResults += math.prod(col)

    f.close()

    return totalResults

print(solve_day_six_part_one())