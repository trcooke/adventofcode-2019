def part1():
    masses = open("input")
    total = 0
    for mass in masses:
        total += fuel(mass)
    return total

def part2():
    masses = open("input")
    total = 0
    for mass in masses:
        reqfuel = fuel(mass)
        total += reqfuel
        reqfuel = fuel(reqfuel)
        while (reqfuel > 0):
            total += reqfuel
            reqfuel = fuel(reqfuel)
    return total

def fuel(mass):
    return int(abs(int(mass)/3.0))-2

print part1()
print part2()
