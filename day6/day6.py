import copy


def load_map(filename):
    map = []
    with open(filename, "r") as input:
        map = [[*line.strip()] for line in input]
    return map


def print_map(map):
    for line in map:
        print("".join(line))
    print("-------------------------")


def find_guard(map):
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if char not in [".", "#"]:
                return (x, y)


def get_dir(map, x, y):
    return ["^", ">", "v", "<"].index(map[y][x])


def can_move_forward(map, x, y, horizontal, vertical):
    return (
        x + horizontal < 0
        or x + horizontal > len(map[0]) - 1
        or y + vertical < 0
        or y + vertical > len(map) - 1
        or map[y + vertical][x + horizontal] != "#"
    )


def move_forward(visited, map, x, y, cur_dir):
    # 0 - North, 1 - East, 2 - South, 3 - West
    vertical = [-1, 0, 1, 0][cur_dir]
    horizontal = [0, 1, 0, -1][cur_dir]
    # map[y][x] = "X"
    in_loop = str(cur_dir) in map[y][x]
    map[y][x] += str(cur_dir)
    visited.add((x, y))
    if can_move_forward(map, x, y, horizontal, vertical):
        return (x + horizontal, y + vertical), cur_dir, in_loop
    else:
        # turn right
        return (x, y), (cur_dir + 1) % 4, in_loop


def out_of_map(map, x, y):
    return x < 0 or x > len(map[0]) - 1 or y < 0 or y > len(map) - 1


def star1():
    orig_map = load_map("input.txt")
    map = copy.deepcopy(orig_map)
    start_pos = find_guard(map)
    cur_pos = find_guard(map)
    cur_dir = get_dir(map, cur_pos[0], cur_pos[1])
    visited = set()
    while not out_of_map(map, cur_pos[0], cur_pos[1]):
        cur_pos, cur_dir, in_loop = move_forward(
            visited, map, cur_pos[0], cur_pos[1], cur_dir
        )
    visited.remove(start_pos)
    loop = 0
    for cell in visited:
        map_copy = copy.deepcopy(orig_map)
        map_copy[cell[1]][cell[0]] = "#"
        cur_pos = start_pos
        cur_dir = get_dir(map_copy, cur_pos[0], cur_pos[1])
        in_loop = False
        print(loop)
        while not out_of_map(map_copy, cur_pos[0], cur_pos[1]):
            cur_pos, cur_dir, in_loop = move_forward(
                set(), map_copy, cur_pos[0], cur_pos[1], cur_dir
            )
            if in_loop:
                loop += 1
                break

    print(loop)


star1()
