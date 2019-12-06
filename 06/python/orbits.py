from sets import Set

def part1():
    orbits = open("input")
    orbitmap = orbittree(orbits)
    depths = depth(orbitmap)
    return sum(depths.values())

def part2():
    orbits = open("input")
    orbitmap = orbittree(orbits)
    return len(orbitsto('YOU', orbitmap) ^ orbitsto('SAN', orbitmap))

def orbittree(orbits):
    orbitmap = {}
    for orbit in orbits:
        (left, right) = orbit.replace("\n","").strip().split(")")
        if left in orbitmap:
            orbitmap[left][1].append(right)
        else:
            orbitmap[left] = ("", [right])
        if right not in orbitmap:
            orbitmap[right] = (left, [])
        else:
            orbitmap[right] = (left, orbitmap[right][1])
    return orbitmap

def depth(orbitmap):
    depths = {}
    comorbit = orbitmap['COM']
    depths['COM'] = 0
    return nextdepth(depths, comorbit[1], orbitmap, 0)

def nextdepth(acc, orbits, orbitmap, d):
    d += 1
    if len(orbits) == 0:
        return acc
    for obj in orbits:
        acc[obj] = d
        nextdepth(acc, orbitmap[obj][1], orbitmap, d)
    return acc

def orbitsto(obj, orbitmap):
    orbits = Set()
    parent = orbitmap[obj][0]
    while parent != '':
        orbits.add(parent)
        parent = orbitmap[parent][0]
    return orbits
    

print part1()
print part2()
