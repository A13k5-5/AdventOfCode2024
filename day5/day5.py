def load_input(filename):
    page_rules = []
    updates = []
    current = page_rules
    with open(filename, "r") as input_file:
        for row in input_file:
            if row == "\n":
                current = updates
            else:
                current.append(
                    row.strip().split("|")
                    if current == page_rules
                    else row.strip().split(",")
                )
    return page_rules, updates


def try_rule(update, rule):
    if rule[0] in update and rule[1] in update:
        return (
            update.index(rule[0]) < update.index(rule[1]),
            update.index(rule[0]),
            update.index(rule[1]),
        )
    return True, -1, -1


def valid_update(update, page_rules):
    for rule in page_rules:
        is_valid, i1, i2 = try_rule(update, rule)
        if not is_valid:
            return False, i1, i2
    return True, -1, -1


def validate_updates(updates, page_rules):
    acc = 0
    for update in updates:
        is_valid, i1, i2 = valid_update(update, page_rules)
        while not is_valid:
            update[i1], update[i2] = update[i2], update[i1]
            is_valid, i1, i2 = valid_update(update, page_rules)
            if is_valid:
                acc += int(update[len(update) // 2])
    print(acc)


page_rules, updates = load_input("input.txt")
validate_updates(updates, page_rules)
