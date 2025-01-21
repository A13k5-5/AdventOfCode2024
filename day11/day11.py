import copy


def load_stones(filename):
    with open(filename, "r") as input:
        for line in input:
            return [int(x) for x in line.split(" ")]


def blink(stones):
    i = 0
    while i < len(stones):
        stone = stones[i]
        stoneLen = len(str(stone))
        if stone == 0:
            stones[i] = 1
        elif stoneLen % 2 == 0:
            first_half = int(str(stone)[: stoneLen // 2])
            second_half = int(str(stone)[stoneLen // 2 :])
            stones.pop(i)
            stones.insert(i, first_half)
            stones.insert(i + 1, second_half)
            i += 1
        else:
            stones[i] *= 2024
        i += 1


def star1():
    stones = load_stones("input.txt")
    for i in range(25):
        blink(stones)
    print(len(stones))


if __name__ == "__main__":
    star1()
