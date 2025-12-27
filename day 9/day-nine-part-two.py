from collections import deque

def floodFill(grid, x, y):
    maxY = len(grid)
    maxX = len(grid[0])
    queue = deque()
    queue.append((x,y))
    while len(queue) != 0:
        (x,y) = queue.popleft()
        if y < 0 or y >= maxY or x < 0 or x >= maxX or grid[y][x] != ".":
            continue
        else:
            grid[y][x] = "X"
            queue.append((x, y+1))
            queue.append((x, y-1))
            queue.append((x+1, y))
            queue.append((x-1, y))

def solve_day_nine_part_one():
    f = open("inputs/day-nine-input.txt", "r")

    verts = []
    areas = []
    xToY = {}
    yToX = {}
    gridXMax = 0
    gridYMax = 0

    for line in f:
        line = line.strip()
        splitLine = line.split(",")
        x = int(splitLine[0])
        y = int(splitLine[1])
        verts.append((x, y))
        
        if x not in xToY:
            xToY[x] = [y]
        else:
            xToY[x].append(y)

        if y not in yToX:
            yToX[y] = [x]
        else:
            yToX[y].append(x)

        gridXMax = max(gridXMax, x)
        gridYMax = max(gridYMax, y)
        
    f.close()
    for x in xToY:
        xToY[x].sort()

    for y in yToX:
        yToX[y].sort()

    # Coordinate compression
    sortedByX = sorted(verts, key=lambda item: item[0])
    sortedByY = sorted(verts, key=lambda item: item[1])

    xCompressed = {}
    xDecompressed = {}
    prev = sortedByX[0][0]
    currMap = 0
    for coord in sortedByX:
        if coord[0] == prev:
            xCompressed[coord[0]] = currMap
            xDecompressed[currMap] = coord[0]
        else:
            currMap += 1
            xCompressed[coord[0]] = currMap
            xDecompressed[currMap] = coord[0]
        prev = coord[0]

    yCompressed = {}
    yDecompressed = {}
    prev = sortedByY[0][1]
    currMap = 0
    for coord in sortedByY:
        if coord[1] == prev:
            yCompressed[coord[1]] = currMap
            yDecompressed[currMap] = coord[1]
        else:
            currMap += 1
            yCompressed[coord[1]] = currMap
            yDecompressed[currMap] = coord[1]
        prev = coord[1]

    # Build grid
    vertsSet = set(verts)
    grid = []
    for yComp in range(0, yCompressed[gridYMax]+1):
        line = []
        for xComp in range(0, xCompressed[gridXMax]+1):
            yDecomp = yDecompressed[yComp]
            xDecomp = xDecompressed[xComp]

            yRange = xToY[xDecomp] if xDecomp in xToY else None
            xRange = yToX[yDecomp] if yDecomp in yToX else None

            yRangeComp = [yCompressed[yRange[0]], yCompressed[yRange[1]]] if yRange else None
            xRangeComp = [xCompressed[xRange[0]], xCompressed[xRange[1]]] if xRange else None

            if (xDecomp,yDecomp) in vertsSet:
                line.append("#")
            else:
                if (xRangeComp and (xRangeComp[0] <= xComp <= xRangeComp[1])) or (yRangeComp and (yRangeComp[0] <= yComp <= yRangeComp[1])):
                    line.append("#")
                else:
                    line.append(".")
        grid.append(line)

    fillStart = None
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y-1][x] == "#" and grid[y][x-1] == "#" and grid[y][x] == ".":
                fillStart = (x,y)
                break
        if fillStart != None:
            break

    # Create filled grid
    filledGrid = []
    for line in grid:
        newLine = []
        for c in line:
            newLine.append(c)
        filledGrid.append(newLine)
    floodFill(filledGrid, fillStart[0], fillStart[1])

    # Create file to look at unfilled grid
    with open("generated-files/day-nine-grid.txt", "w") as writeFile:
        for line in grid:
            lineStr = ""
            for c in line:
                lineStr += c
            writeFile.write(lineStr + "\n")
    writeFile.close()

    # Create file to look at filled grid
    with open("generated-files/day-nine-filled-grid.txt", "w") as writeFile:
        for line in filledGrid:
            lineStr = ""
            for c in line:
                lineStr += c
            writeFile.write(lineStr + "\n")
    writeFile.close()

    # Go through each pair of coordinates and calculate the area if the square is valid
    for i in range(len(verts)):
        for j in range(i+1, len(verts)):
            (x1, y1) = verts[i]
            (x2, y2) = verts[j]

            # Sort so we know what is the smaller and what is the larger of the two x and y values
            xRangeCompressed = sorted([xCompressed[x1], xCompressed[x2]])
            yRangeCompressed = sorted([yCompressed[y1], yCompressed[y2]])

            rectValid = True
            # Check that every part of the top and bottom edge of the rectangle is valid
            for x in range(xRangeCompressed[0], xRangeCompressed[1]+1):
                if filledGrid[yRangeCompressed[0]][x] == "." or filledGrid[yRangeCompressed[1]][x] == ".":
                    rectValid = False
                    break
            
            # Check that every part of the left and right edge of the rectangle is valid
            if rectValid:
                for y in range(yRangeCompressed[0], yRangeCompressed[1]+1):
                    if filledGrid[y][xRangeCompressed[0]] == "." or filledGrid[y][xRangeCompressed[1]] == ".":
                        rectValid = False

            if rectValid:
                area = (abs(x2-x1)+1) * (abs(y2-y1)+1)
                areas.append([verts[i], verts[j], area])

    areas.sort(key=lambda item: item[2], reverse=True)

    largestArea = areas[0]
    print(largestArea)
    return largestArea[2]


print(solve_day_nine_part_one())
