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
        return update.index(rule[0]) < update.index(rule[1])
    return True


def valid_update(update, page_rules):
    for rule in page_rules:
        if not try_rule(update, rule):
            return False
    return True


def validate_updates(updates, page_rules):
    acc = 0
    for update in updates:
        if valid_update(update, page_rules):
            acc += int(update[len(update) // 2])
    print(acc)


page_rules, updates = load_input("input.txt")
# print(valid_update(updates[5], page_rules))
validate_updates(updates, page_rules)
