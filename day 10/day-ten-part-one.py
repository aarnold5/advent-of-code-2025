import itertools
import re

def getButtonCombos(buttonWiring):
    combos = []
    for setLen in range(len(buttonWiring) + 1):
        for subset in itertools.combinations(buttonWiring, setLen):
            combos.append(subset)
    return combos

def pressButtonsAndCheckForValidState(diagram, buttons):
    lights = ["."] * len(diagram)
    for button in buttons:
        for idx in button:
            if lights[idx] == ".":
                lights[idx] = "#"
            elif lights[idx] == "#":
                lights[idx] = "."

    return lights == diagram

def findFewestPresses(diagram, buttonWiring, joltage):
    combos = getButtonCombos(buttonWiring)
    for combo in combos:
        comboIsValid = pressButtonsAndCheckForValidState(diagram, combo)
        if comboIsValid:
            return len(combo)

    return len(buttonWiring)

def solve_day_ten_part_one():
    f = open("inputs/day-ten-input.txt", "r")

    totalFewestPresses = 0

    for line in f:
        splitLine = line.split()
        diagramStr = splitLine[0]
        buttonWiringStr = splitLine[1: len(splitLine)-1]
        joltageStr = splitLine[len(splitLine)-1]

        diagram = []
        for c in diagramStr:
            if c != "[" and c != "]":
                diagram.append(c)

        buttonWiring = []
        for buttonStr in buttonWiringStr:
            buttonNums = [int(s) for s in re.findall(r'\d+', buttonStr)]
            buttonWiring.append(buttonNums)

        joltage = [int(s) for s in re.findall(r'\d+', joltageStr)]
        fewestPresses = findFewestPresses(diagram, buttonWiring, joltage)
        totalFewestPresses += fewestPresses
       
    f.close()

    return totalFewestPresses

print(solve_day_ten_part_one())