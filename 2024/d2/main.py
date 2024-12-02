filename = 'input.txt'
# filename = 'test.txt'
reports = []


def init():
    with open(filename) as file:
        for line in file:
            reports.append([int(i) for i in line.split()])


def is_safe(report):
    current, e, *rest = report
    inc = e > current
    for e in report[1:]:
        if (inc and e < current) or (not inc and e > current) or e == current:
            return False
        if (inc and current + 4 > e) or (not inc and current - 4 < e):
            current = e
        else:
            return False
    # print('solo safe', report)
    return True


def is_safe_removing(report):
    if is_safe(report): return True
    for i in range(len(report)):
        tmp = list(report)
        tmp.pop(i)
        if is_safe(tmp):
            return True
    return False


def part_one():
    init()
    res = 0
    for report in reports:
        res += 1 if is_safe(report) else 0
    print(res)


def part_two():
    init()
    res = 0
    for report in reports:
        if is_safe_removing(report):
            res += 1

    print(int(res))


def main():
    # part_one()
    part_two()


if __name__ == '__main__':
    main()
