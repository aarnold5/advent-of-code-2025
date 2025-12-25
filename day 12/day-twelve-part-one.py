def solve_day_tweleve_part_one():
    f = open("inputs/day-tweleve-input.txt", "r")

    counts = {0:0}
    currShapeNumber = 0
    numRegionsThatCanFit = 0
    
    for line in f:
        splitLine = line.strip().split(":")
        
        if len(splitLine) == 1:
            for c in line:
                if c == "#":
                    counts[currShapeNumber] += 1
            if line == "\n":
                currShapeNumber += 1
                counts[currShapeNumber] = 0

        elif len(splitLine) > 1 and splitLine[1] != "":
            lenAndWidth = [int(x) for x in splitLine[0].split("x") if x.isdigit()]
            numsOfEachShape = [int(x) for x in splitLine[1].split() if x.isdigit()]

            area = lenAndWidth[0] * lenAndWidth[1]

            totalPresents = 0
            for i in range(len(numsOfEachShape)):
                totalPresents += counts[i] * numsOfEachShape[i]

            if totalPresents < area:
                numRegionsThatCanFit += 1
            
    f.close()

    return numRegionsThatCanFit

print(solve_day_tweleve_part_one())