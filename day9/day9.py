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


def run():
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


run()
