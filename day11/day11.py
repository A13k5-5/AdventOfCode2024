def load_stones(filename):
    with open(filename, "r") as input:
        for line in input:
            return [int(x) for x in line.split(" ")]


def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            x = str(stone)
            new_stones.append(int(x[: len(x) // 2]))
            new_stones.append(int(x[len(x) // 2 :]))
        else:
            new_stones.append(2024 * stone)
    return new_stones


def star1():
    stones = load_stones("input.txt")
    for i in range(25):
        stones = blink(stones)
    print(len(stones))


if __name__ == "__main__":
    star1()
