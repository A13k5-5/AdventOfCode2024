from collections import Counter

def load_lists(filename):
    lists = [[], []]
    with open(filename, "r") as input:
        for line in input:
            vals = line.split()
            lists[0].append(int(vals[0]))
            lists[1].append(int(vals[1]))
    return lists


def workout_distances(lists):
    acc_distance = 0
    for lst in lists:
        lst.sort()

    for i in range(min(len(lists[0]), len(lists[1]))):
        acc_distance += abs(lists[0][i] - lists[1][i])
    print(acc_distance)

def star1(lists):
    workout_distances(lists)

def star2(lists):
    acc = 0
    freq_table = Counter(lists[1])
    for val in lists[0]:
        acc += val * freq_table[val]
    print(acc)

if __name__ == "__main__":
    lists = load_lists("input.txt")
    star2(lists)
    