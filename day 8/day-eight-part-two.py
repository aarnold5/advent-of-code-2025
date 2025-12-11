import math


def solve_day_eight_part_two():
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
    
    distI = 0
    circuts = {}
    isSingleCircut = False
    seen = set()
    
    circutsIdx = 0
    while not isSingleCircut:
        (box1, box2, distance) = distances[distI]

        combos.add((box1, box2))
        combos.add((box2, box1))
        seen.add(box1)
        seen.add(box2)

        box1Circut = None
        box2Circut = None
        for c in circuts:
            if box1 in circuts[c]:
                box1Circut = c
            if box2 in circuts[c]:
                box2Circut = c
        
        if box1Circut and not box2Circut:
            circuts[box1Circut].add(box1)
            circuts[box1Circut].add(box2)

        elif box2Circut and not box1Circut:
            circuts[box2Circut].add(box1)
            circuts[box2Circut].add(box2)

        elif box2Circut and box1Circut:
            circuts[box1Circut] = circuts[box1Circut].union(circuts[box2Circut])
            circuts.pop(box2Circut)
        
        else:
            circuts[circutsIdx] = set([box1, box2])
            circutsIdx += 1

        groupNums = list(circuts.keys())

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

                    if foundCombo == True:
                        break
            
            for combo in toCombine:
                if (combo[0] in circuts and combo[1] in circuts):
                    circuts[combo[0]] = circuts[combo[0]].union(circuts[combo[1]])
                    circuts.pop(combo[1])
                    groupNums.remove(combo[1])

        if (len(circuts) == 1 and (len(circuts[list(circuts.keys())[0]]) == len(junctionBoxes) or len(seen) == len(junctionBoxes))):
            break
        
        print(distI)
        distI += 1

    print(distances[distI], distI)
    return distances[distI][0][0] * distances[distI][1][0]

print(solve_day_eight_part_two())