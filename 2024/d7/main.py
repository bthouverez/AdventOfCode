import numpy as np

filename = 'input.txt'
filename = 'test.txt'
equations = []


def init():
    with open(filename) as file:
        for line in file:
            res, *numbers = [int(i) for i in line[:-1].replace(':', '').split()]
            equations.append({res: numbers})


def get_ops(size):
    a = 0
    res = []
    while len(bin(a)) < size +3:
        formatted = format(a, f'#0{size+2}b')[2:]
        res.append(formatted.replace('0', '+').replace('1', '*'))
        a += 1
    return res


def part_one():
    init()
    for eq in equations:
        expected = list(eq.keys())[0]
        print(expected, end=" → ")
        print(eq[expected])
        bins = get_ops(len(eq[expected]) - 1)
        print(bins)
        for ops in bins:
            for ii in range(len(eq[expected])):
                print(eq[expected][ii], ops[ii], eq[expected][ii+1])
        print()

def part_two():
    init()


def main():
    part_one()
    # part_two()


if __name__ == '__main__':
    main()
