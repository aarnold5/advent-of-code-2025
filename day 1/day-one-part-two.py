def solve_day_one_part_two():
    f = open("inputs/day-one-input.txt", "r")
    w = open("demofile4.txt", "a")

    currPos = 50
    countZero = 0 

    for line in f:
        dir = line[0]
        num = int(line[1:])
        additionalCounts = 0
        extra = 0

        if dir == 'L':
            if currPos - num <= 0:
                if currPos != 0:
                    countZero += 1
                    extra = 1
                additionalCounts = (num - currPos) // 100
                countZero += additionalCounts
                w.writelines(" ".join((line[:len(line)-1], str(currPos), str((currPos - num) % 100), str(additionalCounts), str(extra))) + "\n")
            # w.writelines(" ".join((line[:len(line)-1], str(currPos), str((currPos - num) % 100), str(additionalCounts), str(extra))) + "\n")
            print(line[:len(line)-1], currPos, (currPos - num) % 100, additionalCounts, extra)
            currPos = (currPos - num) % 100

        elif dir == 'R':
            if currPos + num > 99:
                # if currPos != 0:
                countZero += 1
                extra = 1
                additionalCounts = (num - (100 - currPos)) // 100
                countZero += additionalCounts
                w.writelines(" ".join((line[:len(line)-1], str(currPos), str((currPos + num) % 100), str(additionalCounts), str(extra))) + "\n")
            # w.writelines(" ".join((line[:len(line)-1], str(currPos), str((currPos + num) % 100), str(additionalCounts), str(extra))) + "\n")
            print(line[:len(line)-1], currPos, (currPos + num) % 100, additionalCounts, extra) #debug by not only logging within the if
            currPos = (currPos + num) % 100

    f.close()
    w.close()
    return countZero

print("The password is " + str(solve_day_one_part_two()))