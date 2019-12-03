def part1():
    wires = open("input")
    wire1 = wires.readline().replace("\n", "").split(",")
    wire2 = wires.readline().replace("\n", "").split(",")

    current = (0,0,0)
    wire1path = {current}
    for path in wire1:
        direction = path[0]
        distance = int(path[1:])
        if direction == 'U':
            for step in range(distance):
                current = (current[0],current[1] + 1, abs(current[0]) + abs(current[1] + 1))
                wire1path.add(current)
        elif direction == 'D':
            for step in range(distance):
                current = (current[0],current[1] - 1, abs(current[0]) + abs(current[1] - 1))
                wire1path.add(current)
        elif direction == 'L':
            for step in range(distance):
                current = (current[0]-1,current[1], abs(current[0] - 1) + abs(current[1]))
                wire1path.add(current)
        elif direction == 'R':
            for step in range(distance):
                current = (current[0]+1,current[1], abs(current[0] + 1) + abs(current[1]))
                wire1path.add(current)

    current = (0,0,0)
    wire2path = {current}
    for path in wire2:
        direction = path[0]
        distance = int(path[1:])
        if direction == 'U':
            for step in range(distance):
                current = (current[0],current[1] + 1, abs(current[0]) + abs(current[1] + 1))
                wire2path.add(current)
        elif direction == 'D':
            for step in range(distance):
                current = (current[0],current[1] - 1, abs(current[0]) + abs(current[1] - 1))
                wire2path.add(current)
        elif direction == 'L':
            for step in range(distance):
                current = (current[0]-1,current[1], abs(current[0] - 1) + abs(current[1]))
                wire2path.add(current)
        elif direction == 'R':
            for step in range(distance):
                current = (current[0]+1,current[1], abs(current[0] + 1) + abs(current[1]))
                wire2path.add(current)
    closest = 1000000000
    for intersection in wire1path.intersection(wire2path):
        if intersection[2] < closest and intersection[2] > 0:
            closest = intersection[2]

    return closest

def part2():
    return 0

print part1()
print part2()
