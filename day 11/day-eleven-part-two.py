def dfs(device, endDevice, connections, numPathsPerDevice):
    if device == endDevice:
        return 1
    elif device == "out":
        return 0
    else:
        totalForThisDevice = 0
        for outDevice in connections[device]:
            if outDevice in numPathsPerDevice:
                totalForThisDevice += numPathsPerDevice[outDevice]
            else:
                num = dfs(outDevice, endDevice, connections, numPathsPerDevice)
                totalForThisDevice += num
        numPathsPerDevice[device] = totalForThisDevice
        return totalForThisDevice
        


def solve_day_eleven_part_one():
    f = open("inputs/day-eleven-input.txt", "r")

    connections = {}
    for line in f:
        splitLine = line.strip().split(":")
        device = splitLine[0]
        outDevices = splitLine[1]
        connections[device] = outDevices.split()
       
    f.close()

    numPathsPerDevice = {}
    svrToFft = dfs("svr", "fft", connections, numPathsPerDevice)
    numPathsPerDevice = {}
    fftToDac = dfs("fft", "dac", connections, numPathsPerDevice)
    numPathsPerDevice = {}
    dacToOut = dfs("dac", "out", connections, numPathsPerDevice)
    return svrToFft * fftToDac * dacToOut

print(solve_day_eleven_part_one())