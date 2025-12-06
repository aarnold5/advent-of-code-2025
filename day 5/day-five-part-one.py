def solve_day_five_part_one():
    f = open("inputs/day-five-input.txt", "r")

    numFresh = 0
    freshIdRanges = []
    readingRanges = True

    for line in f:
        if (line == "\n"):
            readingRanges = False
            continue
        
        if readingRanges:
            line = line.strip()
            [firstNum, secondNum] = line.split("-")
            freshIdRanges.append((int(firstNum), int(secondNum)))
        else:
            id = int(line.strip())
            for idRange in freshIdRanges:
                if idRange[0] <= id <= idRange[1]:
                    numFresh += 1
                    break
            
    f.close()

    return numFresh

print(solve_day_five_part_one())