def solve_day_three_part_two():
    f = open("inputs/day-three-input.txt", "r")

    sum = 0
    for line in f:
        line = line.strip()
        
        maxFirstValue = max(line[:len(line)-11]) # first bank can't be the last two in the line
        maxFirstIndex = line[:len(line)-11].index(maxFirstValue)

        maxSecondValue = max(line[maxFirstIndex+1:len(line)-10]) # the second bank has to come after the first
        maxSecondIndex = line[maxFirstIndex+1:len(line)-10].index(maxSecondValue) + maxFirstIndex+1
        
        maxThirdValue = max(line[maxSecondIndex+1:len(line)-9])
        maxThirdIndex = line[maxSecondIndex+1:len(line)-9].index(maxThirdValue) + maxSecondIndex+1

        maxFourthValue = max(line[maxThirdIndex+1:len(line)-8])
        maxFourthIndex = line[maxThirdIndex+1:len(line)-8].index(maxFourthValue) + maxThirdIndex+1

        maxFifthValue = max(line[maxFourthIndex+1:len(line)-7])
        maxFifthIndex = line[maxFourthIndex+1:len(line)-7].index(maxFifthValue) + maxFourthIndex+1

        maxSixthValue = max(line[maxFifthIndex+1:len(line)-6])
        maxSixthIndex = line[maxFifthIndex+1:len(line)-6].index(maxSixthValue)  + maxFifthIndex+1

        maxSeventhValue = max(line[maxSixthIndex+1:len(line)-5])
        maxSeventhIndex = line[maxSixthIndex+1:len(line)-5].index(maxSeventhValue) + maxSixthIndex+1

        maxEighthValue = max(line[maxSeventhIndex+1:len(line)-4])
        maxEighthIndex = line[maxSeventhIndex+1:len(line)-4].index(maxEighthValue) + maxSeventhIndex+1

        maxNinthValue = max(line[maxEighthIndex+1:len(line)-3])
        maxNinthIndex = line[maxEighthIndex+1:len(line)-3].index(maxNinthValue) + maxEighthIndex+1

        maxTenthValue = max(line[maxNinthIndex+1:len(line)-2])
        maxTenthIndex = line[maxNinthIndex+1:len(line)-2].index(maxTenthValue) + maxNinthIndex+1

        maxEleventhValue = max(line[maxTenthIndex+1:len(line)-1])
        maxEleventhIndex = line[maxTenthIndex+1:len(line)-1].index(maxEleventhValue) + maxTenthIndex+1
        
        maxTwelvethValue = max(line[maxEleventhIndex+1:])

        sum += int(maxFirstValue + maxSecondValue + maxThirdValue + maxFourthValue + maxFifthValue + maxSixthValue + maxSeventhValue + maxEighthValue + maxNinthValue + maxTenthValue + maxEleventhValue + maxTwelvethValue)

    f.close()
    return sum

print(solve_day_three_part_two())