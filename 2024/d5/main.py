import numpy as np

filename = 'input.txt'
# filename = 'test.txt'

raw_rules = []
updates = []

def init():
    with open(filename) as file:
        for line in file:
            if line == '\n':
                break
            raw_rules.append(line[:-1])
        for line in file:
            updates.append([int(i) for i in line[:-1].split(',')])

def is_correct(update):
    for i in range(len(update) - 1):
        before = update[i]
        after = update[i + 1]
        current_rule = str(after) + '|' + str(before)
        if current_rule in raw_rules:
            return current_rule
    return True

def fix(update, rule):
    print('broken',update)
    x = int(rule.split('|')[0])
    y = int(rule.split('|')[1])
    ix = update.index(x)
    iy = update.index(y)
    update[ix], update[iy] = update[iy], update[ix]
    print('fixed',update)
    return update


def part_one():
    init()
    res = 0
    for update in updates:
        if is_correct(update) == True:
            print('CORRECT',update)
            res += update[len(update)//2]
    print(res)


def part_two():
    init()
    res = 0
    for update in updates:
        rule = is_correct(update)
        if rule is not True:
            while rule is not True:
                # print('INCORRECT',update)
                # print('Breaks',rule)
                update = fix(update, rule)
                rule = is_correct(update)
                print()
            res += update[len(update)//2]
    print(res)


def main():
    # part_one()
    part_two()


if __name__ == '__main__':
    main()
