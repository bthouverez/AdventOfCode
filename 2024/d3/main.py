import re

filename = 'input.txt'
# filename = 'test2.txt'
memory = ""


def init():
    global memory
    with open(filename) as file:
        for line in file:
            memory += line


def calc_doable(s):
    x = re.findall(r'mul\(\d+,\d+\)', s)
    print(memory)
    print(x)
    res = 0
    for op in x:
        a, b = [int(i) for i in op[4:-1].split(',')]
        res += a * b
    return res


def part_one():
    init()
    res = calc_doable(memory)
    print(res)


def part_two():
    init()
    data = {}
    x = re.finditer(r'mul\(\d+,\d+\)', memory)
    for m in x:
        data[m.start(0)] = m[0]
    x = re.finditer(r'don\'t\(\)', memory)
    for m in x:
        data[m.start(0)] = 'dt'

    x = re.finditer(r'do\(\)', memory)
    for m in x:
        data[m.start(0)] = 'do'
    print(data)
    do = True
    todo = ""
    for e in sorted(data.keys()):
        if data[e] == 'dt':
            do = False
        elif data[e] == 'do':
            do = True
        else:
            if do:
                todo += data[e]

    res = calc_doable(todo)
    print(res)


def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
