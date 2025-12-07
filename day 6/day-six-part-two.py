import math


def solve_day_six_part_two():
    f = open("inputs/day-six-input.txt", "r")

    numbers = []
    firstLine = True

    for line in f:
        if firstLine:
            for c in line:
                if (c != "\n"):
                    numbers.append([c])
            firstLine = False
        else:
            for i in range(len(line)):
                if (line[i] != "\n"):
                    numbers[i].append(line[i])

    totalResults = 0

    lastOp = ""
    trueNums = []
    for i in range(len(numbers)):
        row = numbers[i]

        if (row[len(row)-1] != " " and row[len(row)-1] != "\n"):
            lastOp = row[len(row)-1]
        
        trueNum = ""
        for c in row:
            if c.isnumeric():
                trueNum += c

        if i == len(numbers)-1:
            trueNums.append(int(trueNum))

        if trueNum == "" or i == len(numbers)-1:
            if lastOp == '+':
                totalResults += sum(trueNums)
            elif lastOp == '*':
                totalResults += math.prod(trueNums)
            trueNums = []
        else:
            trueNums.append(int(trueNum))

    f.close()

    return totalResults


print(solve_day_six_part_two())