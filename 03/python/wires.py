def part1():
    wires = open("input")
    wire1 = wires.readline().replace("\n", "").split(",")
    wire2 = wires.readline().replace("\n", "").split(",")
    
    wire1path = getPath(wire1)
    wire2path = getPath(wire2)

    closest = 1000000000
    for intersection in set(wire1path).intersection(wire2path):
        if intersection[2] < closest and intersection[2] > 0:
            closest = intersection[2]

    return closest

def part2():
    wires = open("input")
    wire1 = wires.readline().replace("\n", "").split(",")
    wire2 = wires.readline().replace("\n", "").split(",")
    
    wire1path = getPath(wire1)
    wire2path = getPath(wire2)

    leaststeps = 100000000
    for intersection in set(wire1path).intersection(wire2path):
        totalsteps = wire1path.index(intersection) + wire2path.index(intersection)
        if totalsteps < leaststeps and totalsteps > 0:
            leaststeps = totalsteps
    return leaststeps

def getPath(wire):
    current = (0,0,0)
    wirepath = [current]
    for path in wire:
        direction = path[0]
        distance = int(path[1:])
        if direction == 'U':
            for step in range(distance):
                current = (current[0],current[1] + 1, abs(current[0]) + abs(current[1] + 1))
                wirepath.append(current)
        elif direction == 'D':
            for step in range(distance):
                current = (current[0],current[1] - 1, abs(current[0]) + abs(current[1] - 1))
                wirepath.append(current)
        elif direction == 'L':
            for step in range(distance):
                current = (current[0]-1,current[1], abs(current[0] - 1) + abs(current[1]))
                wirepath.append(current)
        elif direction == 'R':
            for step in range(distance):
                current = (current[0]+1,current[1], abs(current[0] + 1) + abs(current[1]))
                wirepath.append(current)
    return wirepath

print part1()
print part2()
