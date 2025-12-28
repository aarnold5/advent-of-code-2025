import re
import numpy as np
from sympy import Matrix

def getMinButtonPresses(buttonWiring, joltage):
    maxPressesPerButton = {}
    positionsToButtons = {}
    for buttonIdx in range(len(buttonWiring)):
        button = buttonWiring[buttonIdx]
        maxPress = 1000000000000000000000000000000000000
        for idx in button:
            maxPress = min(joltage[idx], maxPress)
            if idx in positionsToButtons:
                positionsToButtons[idx].append(buttonIdx) 
            else:
                positionsToButtons[idx] = [buttonIdx]
        maxPressesPerButton[buttonIdx] = maxPress

    positionsToButtonsList = []
    for pos in positionsToButtons:
        positionsToButtonsList.append((pos, positionsToButtons[pos]))

    positionsToButtonsList.sort(key=lambda item: item[1][0])

    matrix = []
    for entry in positionsToButtonsList:
        row = []
        buttonIdx = entry[0]
        ones = entry[1]
        onesIdx = 0
        for i in range(len(buttonWiring)):
            if onesIdx < len(ones) and i == ones[onesIdx]:
                row.append(1)
                onesIdx += 1
            else:
                row.append(0)
        row.append(joltage[buttonIdx])
        matrix.append(row)

    symPyMatrx = Matrix(matrix)
    rref = symPyMatrx.rref()
    rrefMatrix = np.array(rref[0])
    pivots = rref[1]

    for row in rrefMatrix:
        print(row)

    pivotsSet = set(pivots)
    notPivots = []
    for i in range(len(buttonWiring)):
        if i not in pivotsSet:
            notPivots.append(i)

    if len(notPivots) == 0:
        totalSum = 0
        for row in rrefMatrix:
            totalSum += row[len(row)-1]
        return totalSum

    elif len(notPivots) == 1:
        freeVar0 = notPivots[0]
        minSum = None
        for s in range(maxPressesPerButton[freeVar0]+1):
            totalSum = 0
            invalidRow = False
            for row in rrefMatrix:
                rowTotal = row[len(row)-1] - row[freeVar0]*s
                if rowTotal < 0 or rowTotal % 1 != 0:
                    invalidRow = True
                    break
                else:
                    totalSum += rowTotal
            if invalidRow:
                continue
            totalSum += s
            
            if not minSum or totalSum < minSum:
                minSum = totalSum
        return minSum

    elif len(notPivots) == 2:
        freeVar0 = notPivots[0]
        freeVar1 = notPivots[1]
        minSum = None
        for s in range(maxPressesPerButton[freeVar0]+1):
            for t in range(maxPressesPerButton[freeVar1]+1):
                totalSum = 0
                invalidRow = False
                for row in rrefMatrix:
                    rowTotal = row[len(row)-1] - row[freeVar0]*s - row[freeVar1]*t
                    if rowTotal < 0 or rowTotal % 1 != 0:
                        invalidRow = True
                        break
                    else:
                        totalSum += rowTotal
                if invalidRow:
                    continue
                totalSum += s + t

                if not minSum or totalSum < minSum:
                    minSum = totalSum
        return minSum

    elif len(notPivots) == 3:
        freeVar0 = notPivots[0]
        freeVar1 = notPivots[1]
        freeVar2 = notPivots[2]
        minSum = None
        for s in range(maxPressesPerButton[freeVar0]+1):
            for t in range(maxPressesPerButton[freeVar1]+1):
                for u in range(maxPressesPerButton[freeVar2]+1):
                    totalSum = 0
                    invalidRow = False
                    for row in rrefMatrix:
                        rowTotal = row[len(row)-1] - row[freeVar0]*s - row[freeVar1]*t - row[freeVar2]*u
                        if rowTotal < 0 or rowTotal % 1 != 0:
                            invalidRow = True
                            break
                        else:
                            totalSum += rowTotal
                    if invalidRow:
                        continue
                    totalSum += s + t + u

                    if not minSum or totalSum < minSum:
                        minSum = totalSum
        return minSum

    return 0

def solve_day_ten_part_one():
    f = open("inputs/day-ten-input.txt", "r")

    totalFewestPresses = 0

    for line in f:
        splitLine = line.split()
        buttonWiringStr = splitLine[1: len(splitLine)-1]
        joltageStr = splitLine[len(splitLine)-1]

        buttonWiring = []
        for buttonStr in buttonWiringStr:
            buttonNums = [int(s) for s in re.findall(r'\d+', buttonStr)]
            buttonWiring.append(buttonNums)

        joltage = [int(s) for s in re.findall(r'\d+', joltageStr)]

        fewestPresses = getMinButtonPresses(buttonWiring, joltage)
        print(fewestPresses)
        totalFewestPresses += fewestPresses

    f.close()

    return totalFewestPresses

print(solve_day_ten_part_one())