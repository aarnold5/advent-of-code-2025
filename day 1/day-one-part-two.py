def solve_day_one_part_two():
    f = open("inputs/day-one-input.txt", "r")

    currPos = 50
    countZero = 0 

    for line in f:
        dir = line[0]
        num = int(line[1:])
        additionalCounts = 0

        if dir == 'L':
            if currPos - num <= 0:
                if currPos != 0:
                    countZero += 1
                additionalCounts = (num - currPos) // 100
                countZero += additionalCounts
            currPos = (currPos - num) % 100

        elif dir == 'R':
            if currPos + num > 99:
                countZero += 1
                additionalCounts = (num - (100 - currPos)) // 100
                countZero += additionalCounts
            currPos = (currPos + num) % 100

    f.close()
    return countZero

print("The password is " + str(solve_day_one_part_two()))