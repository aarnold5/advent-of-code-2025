from collections import deque


def solve_day_eleven_part_one():
    f = open("inputs/day-eleven-input.txt", "r")

    connections = {}

    for line in f:
        splitLine = line.strip().split(":")
        device = splitLine[0]
        outDevices = splitLine[1]
        connections[device] = outDevices.split()
       
    f.close()

    queque = deque()
    queque.append("you")
    ways = 0
    while len(queque) > 0:
        device = queque.popleft()
        if device != "out":
            for outDevice in connections[device]:
                queque.append(outDevice)
        else:
            ways +=1

    return ways

print(solve_day_eleven_part_one())