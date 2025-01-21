def load_input(filename):
    mountains = []
    with open(filename, "r") as input:
        for line in input:
            mountains.append([int(c) for c in line.strip()])
    return mountains


def find_all_zeros(mountains):
    start_coords = set()
    for y, row in enumerate(mountains):
        for x in range(len(row)):
            if row[x] == 0:
                start_coords.add((x, y))
    return start_coords


def get_neighbours(mountains, x, y):
    neighbors = []
    rows = len(mountains)
    cols = len(mountains[0]) if rows > 0 else 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < cols and 0 <= new_y < rows:
            neighbors.append((new_x, new_y))
        else:
            neighbors.append(None)

    return neighbors


def recur(mountains, cur_x, cur_y, counter, visited_nines):
    curVal = mountains[cur_y][cur_x]
    if curVal == 9 and (cur_x, cur_y) not in visited_nines:
        counter[0] += 1
        visited_nines.add((cur_x, cur_y))
        return
    neighbours = get_neighbours(mountains, cur_x, cur_y)
    for neighbour in neighbours:
        if neighbour is None:
            continue
        neighbourVal = mountains[neighbour[1]][neighbour[0]]
        if neighbourVal == curVal + 1:
            recur(mountains, neighbour[0], neighbour[1], counter, visited_nines)


def star1():
    mountains = load_input("input.txt")
    start_coords = find_all_zeros(mountains)
    counter = [0]
    for start in start_coords:
        visited_nines = set()
        cur_x, cur_y = start
        recur(mountains, cur_x, cur_y, counter, visited_nines)
    print(counter)


def recur2(mountains, cur_x, cur_y, counter):
    curVal = mountains[cur_y][cur_x]
    if curVal == 9 and (cur_x, cur_y):
        counter[0] += 1
        return
    neighbours = get_neighbours(mountains, cur_x, cur_y)
    for neighbour in neighbours:
        if neighbour is None:
            continue
        neighbourVal = mountains[neighbour[1]][neighbour[0]]
        if neighbourVal == curVal + 1:
            recur2(mountains, neighbour[0], neighbour[1], counter)


def star2():
    mountains = load_input("input.txt")
    start_coords = find_all_zeros(mountains)
    counter = [0]
    for start in start_coords:
        cur_x, cur_y = start
        recur2(mountains, cur_x, cur_y, counter)
    print(counter)


star2()
