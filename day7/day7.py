def load_input(filename):
    eqs = []
    with open(filename, "r") as input:
        for line in input:
            split_line = [
                int(num) if num[-1] != ":" else int(num[:-1]) for num in line.split()
            ]
            eqs.append(split_line)
    return eqs


def star1():
    eqs = load_input("input.txt")
