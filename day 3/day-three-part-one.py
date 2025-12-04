def solve_day_three_part_one():
    f = open("inputs/day-three-input.txt", "r")

    sum = 0
    for line in f:
        maxFirstValue = max(line[:len(line)-2]) # first bank can't be the last one in the line
        maxFirstIndex = line.index(maxFirstValue)
        maxSecondValue = max(line[maxFirstIndex+1:]) # the second bank has to come after the first

        sum += int(maxFirstValue + maxSecondValue)
        
    f.close()
    return sum

print(solve_day_three_part_one())