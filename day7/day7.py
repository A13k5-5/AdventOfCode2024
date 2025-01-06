def load_input(filename):
    eqs = []
    with open(filename, "r") as input:
        for line in input:
            split_line = [
                int(num) if num[-1] != ":" else int(num[:-1]) for num in line.split()
            ]
            eqs.append(split_line)
    return eqs


def perform_action(nums, operation, results):
    if len(nums) == 1:
        results.add(nums[0])
        # print(nums[0])
        return

    new_nums = []
    new_nums.append(nums[0] * nums[1] if operation == "mult" else nums[0] + nums[1])
    new_nums += nums[2:]
    perform_action(new_nums, "mult", results)
    perform_action(new_nums, "add", results)


def star1():
    eqs = load_input("input.txt")
    counter = 0
    for eq in eqs:
        wanted_result = eq[0]
        nums = eq[1:]
        results = set()
        perform_action(nums, "mult", results)
        perform_action(nums, "add", results)
        if wanted_result in results:
            counter += wanted_result
    print(counter)


star1()
