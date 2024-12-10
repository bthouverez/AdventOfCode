import numpy as np

filename = 'input.txt'
# filename = 'test.txt'


def init():
    data = []
    with open(filename) as file:
        for line in file:
            if line[-1] == '\n': line = line[:-1]
            data.append((line))
    return data

def find_in_lines(arr):
    cpt = 0
    for line in arr:
        cpt += line.count('XMAS')
        cpt += line.count('SAMX')
    return cpt

def part_one():
    data = init()
    data_rot = []
    CPT = 0
    CPT += find_in_lines(data)
    rotated = list(zip(*data))[::-1]
    for line in rotated:
        data_rot.append(''.join(line))
    CPT += find_in_lines(data_rot)
    for offset in range(-len(data), len(data)):
        diag = [row[i + offset] for i, row in enumerate(data) if 0 <= i + offset < len(row)]
        diag = ''.join(diag)
        CPT += diag.count('XMAS')
        CPT += diag.count('SAMX')

    for offset in range(-len(data_rot), len(data_rot)):
        diag = [row[i + offset] for i, row in enumerate(data) if 0 <= i + offset < len(row)]
        diag = ''.join(diag)
        CPT += diag.count('XMAS')
        CPT += diag.count('SAMX')
    print(CPT)

def part_two():
   pass


def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
