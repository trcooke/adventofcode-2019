import copy

def part1():
    memory = getinput("input")
    memory[1] = 12
    memory[2] = 2
    return program(memory)

def part2():
    originalmemory = getinput("input")
    for noun in range(100):
        for verb in range(100):
            memory = copy.copy(originalmemory)
            memory[1] = noun
            memory[2] = verb
            output = program(memory)
            if output == 19690720:
                return 100 * noun + verb
    return 0

def getinput(filename):
    rawinput = open(filename)
    return map(int, rawinput.readline().replace("\n", "").split(","))

def program(memory):
    i = 0
    while memory[i] != 99:
        if memory[i] == 1:
            memory[memory[i+3]] = memory[memory[i+1]] + memory[memory[i + 2]]
            i += 4
        elif memory[i] == 2:
            memory[memory[i+3]] = memory[memory[i+1]] * memory[memory[i+2]]
            i += 4
    return memory[0]

print part1()
print part2()

