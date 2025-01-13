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


def find_file(file_id, disk):
    for i, cell in enumerate(disk):
        if cell[0] == file_id:
            return i
    return None


def find_suitable_space(size, disk):
    for i in range(len(disk)):
        if disk[i][0] == None and disk[i][1] >= size:
            return i
    return None


def connect_spaces(disk):
    for i, cell in enumerate(disk):
        while disk[i][1] <= 0:
            disk.pop(i)
        if disk[i][0] == None:
            while i < len(disk) - 1 and disk[i + 1][0] == None:
                disk[i] = (disk[i][0], disk[i][1] + disk[i + 1][1])
                disk.pop(i + 1)


def swap(space, file, disk):
    the_file = disk.pop(file)
    disk.insert(file, (None, the_file[1]))
    disk[space] = (None, disk[space][1] - the_file[1])
    disk.insert(space, the_file)


def convert_disk_into_list(disk):
    actual_disk = []
    for cell in disk:
        for _ in range(cell[1]):
            actual_disk.append(cell[0])
    return actual_disk


def id_mult2(disk):
    acc = 0
    for i, cell in enumerate(disk):
        if cell != None:
            acc += i * cell
    print(acc)
    return acc


def star2():
    disk_map = load_input("input.txt")
    disk = []
    last_file_id = 0
    for i, num in enumerate(disk_map):
        if i % 2 == 0:
            disk.append((i // 2, num))
            last_file_id = i // 2
        else:
            disk.append((None, num))

    # print(disk)

    for cur_file_id in range(last_file_id, -1, -1):
        file_index = find_file(cur_file_id, disk)
        # print(f"file: {disk[file_index]}")
        suitable_space_index = find_suitable_space(disk[file_index][1], disk)
        if suitable_space_index:
            # print(f"Suitable space: {disk[suitable_space_index]}")
            if suitable_space_index < file_index:
                swap(suitable_space_index, file_index, disk)
                connect_spaces(disk)
                # print(disk)
        else:
            print("No suitable space")
    actual_disk = convert_disk_into_list(disk)
    print(actual_disk)
    id_mult2(actual_disk)


# star1()
star2()
