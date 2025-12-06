# for part two, loop until the number of accessible toilet paper is zero
# update the map and run again

def printMap(grid):
    for y in range(len(grid)):
        line = ""
        for x in range(len(grid[0])):
            line += grid[y][x]
        print(line+"\n")
    print("\n")

def solve_day_four_part_two():
    f = open("inputs/day-four-input.txt", "r")

    grid = []
    accessibleRolls = None
    totalRemoved = 0

    for line in f:
        line = line.strip()
        row = []
        for c in line:
            row.append(c)
        grid.append(row)
        
    f.close()
    
    while accessibleRolls == None or accessibleRolls > 0:
        accessibleRolls = 0
        for x in range(len(line)):
            for y in range(len(grid)):
                if (grid[y][x] == "@"):
                    numAdjacent = 0
                    if (x-1 >= 0):
                        numAdjacent += (1 if grid[y][x-1] == "@" else 0)
                        if (y-1 >= 0):
                            numAdjacent += (1 if grid[y-1][x-1] == "@" else 0)
                        if (y+1 < len(grid)):
                            numAdjacent += (1 if grid[y+1][x-1] == "@" else 0)
                        
                    if (x + 1 < len(line)):
                        numAdjacent += (1 if grid[y][x+1] == "@" else 0)
                        if (y-1 >= 0):
                            numAdjacent += (1 if grid[y-1][x+1] == "@" else 0)
                        if (y+1 < len(grid)):
                            numAdjacent += (1 if grid[y+1][x+1] == "@" else 0)

                    if (y-1 >= 0):
                        numAdjacent += (1 if grid[y-1][x] == "@" else 0)
                    if (y+1 < len(grid)):
                        numAdjacent += (1 if grid[y+1][x] == "@" else 0)

                    if numAdjacent < 4:
                        grid[y][x] = "x"
                        totalRemoved += 1
                        if accessibleRolls:
                            accessibleRolls += 1
                        else : accessibleRolls = 1

    return totalRemoved

print(solve_day_four_part_two())

