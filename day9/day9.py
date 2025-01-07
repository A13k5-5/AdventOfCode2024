def load_input(filename):
    disk_map = []
    with open(filename, "r") as input:
        for line in input:
            disk_map = [int(c) for c in line.strip()]
    return disk_map


def extract_map(disk_map):
    map = []
    for i, num in enumerate(disk_map):
        if i % 2 == 0:
            map += [i // 2] * num
        else:
            map += [None] * num
    return map


def id_mult(map):
    acc = 0
    for i, num in enumerate(map):
        if num == None:
            break
        acc += i * num
    return acc


def star1():
    disk_map = load_input("input.txt")
    map = extract_map(disk_map)
    last = len(map) - 1
    first_free = map.index(None)
    while first_free < last:
        map[first_free], map[last] = map[last], map[first_free]
        while map[last] == None:
            last -= 1
        while map[first_free] != None:
            first_free += 1
    print(id_mult(map))


def find_last_file(disk):
    i = len(disk) - 1
    while disk[i][0] == None:
        i -= 1
    return i


def find_first_space(disk):
    i = 0
    while disk[i][0] != None:
        i += 1
    return i


def star2():
    disk_map = load_input("input.txt")
    print(disk_map)
    disk = []
    for i, num in enumerate(disk_map):
        if i % 2 == 0:
            disk.append((i // 2, num))
        else:
            disk.append((None, num))
    print(disk)
    last = find_last_file(disk)


# star1()
star2()
