def solve_day_five_part_two():
    f = open("inputs/day-five-input.txt", "r")

    freshIdRanges = []

    for line in f:
        if (line == "\n"):
            break
        
        line = line.strip()
        [firstNum, secondNum] = line.split("-")
        freshIdRanges.append([int(firstNum), int(secondNum)])
            
    f.close()

    freshIdRanges.sort(key=lambda item: item[0])

    i = 1
    while i < len(freshIdRanges):
        currIdRange = freshIdRanges[i]
        prevIdRange = freshIdRanges[i-1]
        if currIdRange[0] <= prevIdRange[1]:
            if currIdRange[1] > prevIdRange[1]:
                prevIdRange[1] = currIdRange[1]
                freshIdRanges.pop(i)
            else:
                freshIdRanges.pop(i)
        else:
            i += 1

    totalFreshIds = 0
    for idRange in freshIdRanges:
        totalFreshIds += idRange[1] - idRange[0] + 1
    return totalFreshIds

print(solve_day_five_part_two())