def solve_day_four_part_one():
    f = open("inputs/day-four-input.txt", "r")

    grid = []
    accessibleRolls = 0 
    for line in f:
        line = line.strip()
        grid.append(line)
        
    f.close()

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
                    accessibleRolls += 1

    return accessibleRolls

print(solve_day_four_part_one())