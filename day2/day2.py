def load_input(filename):
    lists = []
    with open(filename, "r") as input:
        for line in input:
            lists.append([int(x) for x in line.split()])
    return lists


def isSafe(row):
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


def star2(input):
    # Brute force - try removing every single one
    acc = 0
    for row in input:
        if isSafe(row):
            acc += 1
        else:
            for i in range(len(row)):
                rowCopy = row.copy()
                del rowCopy[i]
                if isSafe(rowCopy):
                    acc += 1
                    break
    print(acc)


if __name__ == "__main__":
    input = load_input("input.txt")
    star2(input)
