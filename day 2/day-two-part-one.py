def solve_day_two_part_one():
    f = open("inputs/day-two-input.txt", "r")

    for line in f:
        sum = 0
        ranges = line.split(",")
        for r in ranges:
            [id1, id2] = r.split('-')
            for num in range(int(id1), int(id2)+1):
                stringNum = str(num)
                if len(stringNum) % 2 == 0:
                    firstHalf = stringNum[:len(stringNum)//2]
                    secondHalf = stringNum[len(stringNum)//2:]
                    if firstHalf == secondHalf:
                        sum += num
    f.close()
    return sum

print(solve_day_two_part_one())