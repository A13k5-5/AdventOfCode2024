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
        return update.index(rule[0]) < update.index(rule[1]), update.index(rule[1])
    return True, 0


def valid_update(update, page_rules):
    for rule in page_rules:
        is_valid, invalid_index = try_rule(update, rule)
        if not is_valid:
            return False, invalid_index
    return True, -1


def valid_updates_sum(updates, page_rules):
    acc = 0
    for update in updates:
        is_valid, invalid_index = valid_update(update, page_rules)
        if is_valid:
            acc += int(update[len(update) // 2])
    print(acc)


page_rules, updates = load_input("input.txt")
valid_updates_sum(updates, page_rules)
