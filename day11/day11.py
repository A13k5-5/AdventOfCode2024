def load_stones(filename):
    with open(filename, "r") as input:
        for line in input:
            return [int(x) for x in line.strip().split(" ")]


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


cache = {}


def ans(x, n):
    if n == 0:
        return 1
    if (x, n) not in cache:
        result = 0
        if x == 0:
            result = ans(1, n - 1)
        elif len(str(x)) % 2 == 0:
            x = str(x)
            result += ans(int(x[: len(x) // 2]), n - 1)
            result += ans(int(x[len(x) // 2 :]), n - 1)
        else:
            result = ans(2024 * x, n - 1)
        cache[(x, n)] = result
    return cache[(x, n)]


def star2():
    stones = load_stones("input.txt")
    res = 0
    for stone in stones:
        res += ans(stone, 75)
    print(res)


if __name__ == "__main__":
    star2()
