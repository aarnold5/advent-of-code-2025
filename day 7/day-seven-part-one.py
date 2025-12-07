def print_grid(grid):
    for line in grid:
        print(line)
    print('\n')


def solve_day_seven_part_one():
    f = open("inputs/day-seven-input.txt", "r")

    grid = []

    for line in f:
        line = line.strip()
        lineSplit = []
        for c in line:
            lineSplit.append(c)
        grid.append(lineSplit)

    f.close()

    print_grid(grid)

    timesSpit = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'S' or grid[y][x] == '|':
                if y < len(grid) - 1 and grid[y+1][x] == '.':
                    grid[y+1][x] = '|'
                elif y < len(grid) - 1 and grid[y+1][x] == '^':
                    timesSpit += 1
                    if x-1 >= 0:
                        grid[y+1][x-1] = '|'
                    if x+1 < len(grid[y]):
                        grid[y+1][x+1] = '|'

    print_grid(grid)
    return timesSpit
                    

print(solve_day_seven_part_one())