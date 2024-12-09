import re


def load_input(filename):
    input = ""
    with open(filename, "r") as input_file:
        for line in input_file:
            input += line
    return input


def detect_mul(input):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, input)
    result = [(int(x), int(y)) for x, y in matches]
    return result


def multiply(tuples):
    acc = 0
    for tuple in tuples:
        acc += tuple[0] * tuple[1]
    print(acc)
    return acc


input = load_input("input.txt")
tuples = detect_mul(input)
multiply(tuples)
