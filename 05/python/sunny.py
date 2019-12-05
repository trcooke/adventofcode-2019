import copy

def part1():
    memory = getinput("input")
    program(memory, 1)

def part2():
    memory = getinput("input")
    program(memory, 5)

def getinput(filename):
    rawinput = open(filename)
    return map(int, rawinput.readline().replace("\n", "").split(","))

def program(memory, instruction):
    i = 0
    while opcode(memory[i]) != 99:
        if opcode(memory[i]) == 1:
            memory[memory[i+3]] = param1(memory, i) + param2(memory, i)
            i = newpointer(i, 4, memory[i+3])
        elif opcode(memory[i]) == 2:
            memory[memory[i+3]] = param1(memory, i) * param2(memory, i)
            i = newpointer(i, 4, memory[i+3])
        elif opcode(memory[i]) == 3:
            memory[memory[i+1]] = instruction
            i = newpointer(i, 2, memory[i+1])
        elif opcode(memory[i]) == 4:
            print param1(memory,i)
            i += 2
        elif opcode(memory[i]) == 5:
            if param1(memory, i) != 0:
                i = param2(memory, i)
            else:
                i += 3
        elif opcode(memory[i]) == 6:
            if param1(memory,i) == 0:
                i = param2(memory,i)
            else:
                i += 3
        elif opcode(memory[i]) == 7:
            if param1(memory,i) < param2(memory,i):
                memory[memory[i+3]] = 1
            else:
                memory[memory[i+3]] = 0
            i = newpointer(i, 4, memory[i+3])
        elif opcode(memory[i]) == 8:
            if param1(memory,i) == param2(memory,i):
                memory[memory[i+3]] = 1
            else:
                memory[memory[i+3]] = 0
            i = newpointer(i, 4, memory[i+3])

def newpointer(i, n, modified):
    if i != modified:
        return i + n
    else:
        return i

def opcode(code):
    return (code/10)%10 * 10 + code%10

def param1(mem, i):
    if param1mode(mem[i]) == 1:
        return mem[i+1]
    else:
        return mem[mem[i+1]]

def param2(mem, i):
    if param2mode(mem[i]) == 1:
        return mem[i+2]
    else:
        return mem[mem[i+2]]

def param1mode(opcode):
    return (opcode/100)%10

def param2mode(opcode):
    return (opcode/1000)%10

part1()
part2()

