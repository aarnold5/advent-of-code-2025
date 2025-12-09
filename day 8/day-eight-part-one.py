import math


def solve_day_eight_part_one(numShortestDistances):
    f = open("inputs/day-eight-input.txt", "r")

    junctionBoxes = []
    distances = []
    combos = set()

    for line in f:
        line = line.strip()
        splitLine = line.split(",")
        junctionBoxes.append((int(splitLine[0]), int(splitLine[1]), int(splitLine[2])))
        
    f.close()

    for i in range(len(junctionBoxes)):
        for j in range(i+1, len(junctionBoxes)):
            (x1, y1, z1) = junctionBoxes[i]
            (x2, y2, z2) = junctionBoxes[j]
            distance = math.sqrt(pow(x2-x1, 2) + pow(y2-y1,2) + pow(z2-z1,2))
            distances.append([junctionBoxes[i], junctionBoxes[j], distance])
    
    distances.sort(key=lambda item: item[2])
    
    shortestDistances = distances[:numShortestDistances]
    boxesSeen = {}
    circutIdx = 0

    for entry in shortestDistances:
        (box1, box2, distance) = entry

        combos.add((box1, box2))
        combos.add((box2, box1))

        if len(boxesSeen) == 0:
            boxesSeen[box1] = 0
            boxesSeen[box2] = 0

        if box1 in boxesSeen and box2 in boxesSeen:
            for box in boxesSeen:
                if boxesSeen[box] == boxesSeen[box2]:
                    boxesSeen[box] = boxesSeen[box1]
        elif box1 in boxesSeen:
            boxesSeen[box1] = boxesSeen[box1]
            boxesSeen[box2] = boxesSeen[box1]
        elif box2 in boxesSeen:
            boxesSeen[box1] = boxesSeen[box2]
            boxesSeen[box2] = boxesSeen[box2]
        else:
            circutIdx += 1
            boxesSeen[box1] = circutIdx
            boxesSeen[box2] = circutIdx


    boxCounts = {}
    circuts = {}
    for box in boxesSeen:
        if boxesSeen[box] in boxCounts:
            boxCounts[boxesSeen[box]] += 1
        else:
            boxCounts[boxesSeen[box]] = 1

        if boxesSeen[box] in circuts:
            circuts[boxesSeen[box]].add(box)
        else:
            circuts[boxesSeen[box]] = set()
            circuts[boxesSeen[box]].add(box)

    groupNums = list(boxCounts.keys())

    toCombine = set()
    first = True
    while len(toCombine) > 0 or first:
        first = False
        toCombine = set()
        for i in range(0, len(groupNums)):
            for j in range(i+1, len(groupNums)):
                groupNum1 = groupNums[i]
                groupNum2 = groupNums[j]
                
                foundCombo = False
                for n1 in circuts[groupNum1]:
                    for n2 in circuts[groupNum2]:
                        if (n1, n2) in combos or (n2, n1) in combos:
                            toCombine.add((groupNum1, groupNum2))
                            foundCombo = True
                            break
                    
                    if foundCombo == True:
                        break
        
        print("Combine", toCombine)
        for combo in toCombine:
            circuts[combo[0]] = circuts[combo[0]].union(circuts[combo[1]])
            if circuts[combo[1]]:
                circuts[combo[1]].pop()  

    lengths = []
    for c in circuts:
        lengths.append(len(circuts[c]))
    sortedCircutSize = sorted(list(lengths), reverse=True)
        
    return math.prod(sortedCircutSize[:3])

print(solve_day_eight_part_one(1000))