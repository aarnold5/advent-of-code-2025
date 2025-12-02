def solve_day_one_part_one():
    f = open("inputs/day-one-input.txt", "r")

    currPos = 50
    countZero = 0
    for line in f:
        dir = line[0]
        num = line[1:]

        if dir == 'L':
            currPos = (currPos - int(num)) % 100
        elif dir == 'R':
            currPos = (currPos + int(num)) % 100

        if currPos == 0:
            countZero += 1

    f.close()
    return countZero

print("The password is " + str(solve_day_one_part_one()))