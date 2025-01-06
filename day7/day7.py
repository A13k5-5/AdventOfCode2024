import math


def load_input(filename):
    eqs = []
    with open(filename, "r") as input:
        for line in input:
            split_line = [
                int(num) if num[-1] != ":" else int(num[:-1]) for num in line.split()
            ]
            eqs.append(split_line)
    return eqs


def concat(a, b):
    return int(str(a) + str(b))  # 18 seconds
    # return int(math.pow(10, (int(math.log(b, 10)) + 1)) * a + b) # 18 seconds


def perform_action(nums, operation, results):
    if len(nums) == 1:
        results.add(nums[0])
        return

    new_nums = []
    first_num = 0
    if operation == "mult":
        first_num = nums[0] * nums[1]
    elif operation == "add":
        first_num = nums[0] + nums[1]
    elif operation == "concat":
        first_num = concat(nums[0], nums[1])

    new_nums.append(first_num)
    new_nums += nums[2:]
    perform_action(new_nums, "mult", results)
    perform_action(new_nums, "add", results)
    perform_action(new_nums, "concat", results)


def star1():
    eqs = load_input("input.txt")
    counter = 0
    for eq in eqs:
        wanted_result = eq[0]
        nums = eq[1:]
        results = set()
        perform_action(nums, "mult", results)
        perform_action(nums, "add", results)
        perform_action(nums, "concat", results)
        if wanted_result in results:
            counter += wanted_result
    print(counter)


star1()
# print(concat(15, 16))
