import math


def solve_day_nine_part_one():
    f = open("inputs/day-nine-input.txt", "r")

    verts = []
    areas = []

    for line in f:
        line = line.strip()
        splitLine = line.split(",")
        verts.append((int(splitLine[0]), int(splitLine[1])))
        
    f.close()

    for i in range(len(verts)):
        for j in range(i+1, len(verts)):
            (x1, y1) = verts[i]
            (x2, y2) = verts[j]
            area = (abs(x2-x1)+1) * (abs(y2-y1)+1)
            areas.append([verts[i], verts[j], area])
    
    areas.sort(key=lambda item: item[2], reverse=True)

    largestArea = areas[0]   
    return largestArea[2]

print(solve_day_nine_part_one())