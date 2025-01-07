def load_input(filename):
    map = []
    with open(filename, "r") as input:
        map = [line.strip() for line in input]
    return map


def antenna_positions(map):
    antenna_pos = {}
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell == ".":
                continue
            if cell not in antenna_pos.keys():
                antenna_pos[cell] = [(x, y)]
            else:
                antenna_pos[cell].append((x, y))
    return antenna_pos


def out_of_map(map, x, y):
    return x < 0 or x > len(map[0]) - 1 or y < 0 or y > len(map) - 1


def vector(p1, p2):
    return (p2[0] - p1[0], p2[1] - p1[1])


def add_vector(v, p):
    return (p[0] + v[0], p[1] + v[1])


def star1():
    map = load_input("input.txt")
    antenna_pos = antenna_positions(map)
    antinodes = set()
    for antenna_type in antenna_pos.keys():
        for i, antenna in enumerate(antenna_pos[antenna_type]):
            other_antennas = [a for a in antenna_pos[antenna_type] if a != antenna]
            for a in other_antennas:
                # print(antenna, a)
                # print(vector(antenna, a))
                # print(add_vector(vector(antenna, a), a))
                antinode = add_vector(vector(antenna, a), a)
                if not out_of_map(map, antinode[0], antinode[1]):
                    antinodes.add(antinode)
    print(len(antinodes))


star1()
