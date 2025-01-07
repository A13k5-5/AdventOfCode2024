def load_input(filename):
    map = []
    with open(filename, "r") as input:
        map = [line.strip() for line in input]
    return map


def star1():
    map = load_input("input.txt")
    antenna_pos = {}
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell == ".":
                continue
            if cell not in antenna_pos.keys():
                antenna_pos[cell] = [(x, y)]
            else:
                antenna_pos[cell].append((x, y))


star1()
