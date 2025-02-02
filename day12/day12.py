def load_plants(filename):
    plants = []
    with open(filename, "r") as input:
        for row in input:
            plants.append(list(row.strip()))
    return plants


def get_neighbours(plants, x, y):
    top = down = left = right = None
    if y > 0:
        top = plants[y - 1][x]
    if y < len(plants) - 1:
        down = plants[y + 1][x]

    if x > 0:
        left = plants[y][x - 1]
    if x < len(plants[0]) - 1:
        right = plants[y][x + 1]

    return (top, down, left, right)


def not_same_neighbours(plants, x, y):
    neighbours = get_neighbours(plants, x, y)
    count = 0
    for n in neighbours:
        if n != plants[y][x]:
            count += 1
    return count


def calc_price(areas, perimeters):
    total_price = 0
    for plant in areas:
        total_price += areas[plant] * perimeters[plant]
    return total_price


def star1():
    plants = load_plants("input.txt")
    areas = {}
    perimeters = {}
    for y, row in enumerate(plants):
        for x, plant in enumerate(row):
            if plant in areas:
                areas[plant] += 1
            else:
                areas[plant] = 1

            if plant in perimeters:
                perimeters[plant] += not_same_neighbours(plants, x, y)
            else:
                perimeters[plant] = not_same_neighbours(plants, x, y)
    print(areas)
    print(perimeters)
    print(calc_price(areas, perimeters))


if __name__ == "__main__":
    star1()
