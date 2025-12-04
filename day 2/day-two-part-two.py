import textwrap

def all_slices_equivalent(stringNum, numPieces):
    pieces = textwrap.wrap(stringNum, numPieces)
    for piece in pieces:
        if piece != pieces[0]:
            return False
    return True

def solve_day_two_part_two():
    f = open("inputs/day-two-input.txt", "r")

    for line in f:
        sum = 0
        ranges = line.split(",")
        for r in ranges:
            print("Checking range " + r + "...")
            [id1, id2] = r.split('-')
            for num in range(int(id1), int(id2)+1):
                stringNum = str(num)
                isValid = False
                for subLen in range(1, len(stringNum)//2+1):
                    if (len(stringNum) % subLen) == 0:
                        isValid = all_slices_equivalent(stringNum, subLen)
                        if (isValid):
                            sum += num
                            break
    f.close()
    return sum

print(solve_day_two_part_two())

