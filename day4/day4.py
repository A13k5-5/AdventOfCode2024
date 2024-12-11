def load_input(filename):
    rows = []
    with open(filename, "r") as input_file:
        for row in input_file:
            rows.append(row.strip())
    return rows


def check_horizontal(rows, target):
    acc = 0
    for row in rows:
        for i in range(len(row) - (len(target) - 1)):
            word = row[i : i + 4]
            if word == target or word[::-1] == target:
                acc += 1
    return acc


def check_vertical(rows, target):
    acc = 0
    for y in range(len(rows) - (len(target) - 1)):
        for x in range(len(rows[0])):
            word = ""
            for i in range(len(target)):
                word += rows[y + i][x]
            if word == target or word[::-1] == target:
                acc += 1
    return acc


def check_diagonal_lr_down(rows, target):
    acc = 0
    for y in range(len(rows) - (len(target) - 1)):
        for x in range(len(rows) - (len(target) - 1)):
            word = ""
            for i in range(len(target)):
                word += rows[y + i][x + i]
            if word == target or word[::-1] == target:
                acc += 1
    return acc


def check_diagonal_lr_up(rows, target):
    acc = 0
    for y in range(len(target) - 1, len(rows)):
        for x in range(len(rows) - (len(target) - 1)):
            word = ""
            for i in range(len(target)):
                word += rows[y - i][x + i]
            if word == target or word[::-1] == target:
                acc += 1
    return acc


rows = load_input("input.txt")
the_word = "XMAS"
acc = 0
acc += check_horizontal(rows, the_word)
acc += check_vertical(rows, the_word)
acc += check_diagonal_lr_down(rows, the_word)
acc += check_diagonal_lr_up(rows, the_word)
print(acc)
