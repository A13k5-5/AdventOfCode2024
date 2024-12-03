def load_input(filename):
    lists = []
    with open(filename, "r") as input:
        for line in input:
            lists.append([int(x) for x in line.split()])
    return lists


def isSafe(row):
    max_diff = 0
    increasing = row[1] - row[0] > 0
    for i in range(len(row) - 1):
        diff = row[i + 1] - row[i]

        if (diff > 0) != increasing or abs(diff) > 3 or abs(diff) == 0:
            return False
    return True


def star1(input):
    acc = 0
    for row in input:
        if isSafe(row):
            acc += 1
    print(acc)


if __name__ == "__main__":
    input = load_input("input.txt")
    star1(input)
