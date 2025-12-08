def print_grid(grid):
    for line in grid:
        print(line)
    print('\n')


def solve_day_seven_part_two():
    f = open("inputs/day-seven-input.txt", "r")

    grid = []

    for line in f:
        line = line.strip()
        lineSplit = []
        for c in line:
            lineSplit.append(c)
        grid.append(lineSplit)

    f.close()

    parents = {}
    start = (0, 0)

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'S':
                start = (y,x)

            if grid[y][x] == 'S' or grid[y][x] == '|':
                if y < len(grid) - 1 and (grid[y+1][x] == '.' or grid[y+1][x] == '|'):
                    grid[y+1][x] = '|'
                    
                    # Keep track of what parent coord we came from to get here
                    if (y+1,x) not in parents:
                        parents[(y+1,x)] = []
                    parents[(y+1,x)].append((y,x))

                elif y < len(grid) - 1 and grid[y+1][x] == '^':
                    if x-1 >= 0:
                        grid[y+1][x-1] = '|'

                        # Keep track of what parent coord we came from to get here
                        if (y+1,x-1) not in parents:
                            parents[(y+1,x-1)] = []
                        parents[(y+1,x-1)].append((y,x)) 

                    if x+1 < len(grid[y]):
                        grid[y+1][x+1] = '|'

                        # Keep track of what parent coord we came from to get here
                        if (y+1,x+1) not in parents:
                            parents[(y+1,x+1)] = []
                        parents[(y+1,x+1)].append((y,x))              

    # Intitialize all the beams and the starting point as having been visited once
    for child in parents:
        (y, x) = child
        grid[y][x] = 1
    grid[start[0]][start[1]] = 1

    for child in parents:
        (y, x) = child
        parentListForCurrChild = parents[child]

        # If there is only one parent, the child inherits the parent's count
        if len(parentListForCurrChild) == 1:
            (parentY, parentX) = parentListForCurrChild[0]
            grid[y][x] = grid[parentY][parentX]

        # If there is more than one parent, we count up the counts of all the parents
        else:
            total = 0
            for parent in parentListForCurrChild:
                (parentY, parentX) = parent
                total += grid[parentY][parentX]
            grid[y][x] = total

    # We get the total by adding up all the accumulated counts on the last row
    totalTimelines = 0
    for item in grid[len(grid)-1]:
        if item != '.':
            totalTimelines += item

    return totalTimelines
                    

print(solve_day_seven_part_two())