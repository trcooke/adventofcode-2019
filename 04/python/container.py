def part1():
    (start, end) = map(int, open("input").readline().replace("\n", "").split("-"))
    current = start
    validpasswords = 0
    while current <= end:
        if meetscriteria(current):
            validpasswords += 1
        current += 1
    return validpasswords

def part2():
    (start, end) = map(int, open("input").readline().replace("\n", "").split("-"))
    current = start
    validpasswords = 0
    while current <= end:
        if meetscriteria2(current):
            validpasswords += 1
        current += 1
    return validpasswords

def meetscriteria(password):
    if not sameadjacentdigits(password):
        return False
    if not decreasingdigits(password):
        return False
    return True

def meetscriteria2(password):
    if not sameadjacentdigits2(password):
        return False
    if not decreasingdigits(password):
        return False
    return True

def sameadjacentdigits(password):
    pwstr = str(password)
    for i in range(len(pwstr) - 1):
        if pwstr[i] == pwstr[i+1]:
            return True
    return False

def sameadjacentdigits2(password):
    pwstr = str(password)
    lastdigit = ""
    consecutivedigits = 1
    for digit in pwstr:
        if digit == lastdigit:
            consecutivedigits += 1
        elif consecutivedigits == 2:
            return True
        else:
            consecutivedigits = 1
            lastdigit = digit
    if consecutivedigits == 2:
        return True
    return False

def decreasingdigits(password):
    pwstr = str(password)
    for i in range(len(pwstr) - 1):
        if pwstr[i] > pwstr[i+1]:
            return False
    return True

print part1()
print part2()

