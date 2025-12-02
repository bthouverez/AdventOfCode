import numpy as np


def part_one(filename):
    res = 0
    with open(filename) as f:
        ids = f.readline().strip().split(',')
    for i in ids:
        i = i.split('-')
        start = int(i[0])
        end = int(i[1])
        for j in range(start, end + 1):
            if is_invalid(j):
                res += j
                print(f'Invalid ID found: {j}')
    print(f'Part one: {res}')


def is_invalid(i):
    s = str(i)
    if len(s) % 2 == 1:
        return False
    mid = len(s) // 2
    return s[:mid] == s[mid:]


def part_two(filename):
    res = 0
    with open(filename) as f:
        ids = f.readline().strip().split(',')
    for i in ids:
        i = i.split('-')
        start = int(i[0])
        end = int(i[1])
        for j in range(start, end + 1):
            s = str(j)
            if is_invalid(j):
                print(f'ID with classical pattern match found: {j}, pattern: {s[:len(s) // 2]}')
                res += j
                continue

            pattern = search_pattern(j)
            if pattern is not None:
                b = True
                for e in [s[i:i + len(pattern)] for i in range(0, len(s), len(pattern))]:
                    if e != pattern:
                        b = False
                        break
                if b:
                    res += j
                    print(f'ID with full pattern match found: {j}, pattern: {pattern}')

    print(f'Part two: {res}')


def search_pattern(i):
    s = str(i)
    length = len(s)
    for size in range(1, length // 2 + 1):
        for start in range(0, length - 2 * size + 1):
            if s[start:start + size] == s[start + size:start + 2 * size]:
                return s[start:start + size]
    return None


def main():
    # part_one('input.txt')
    # part_one('test.txt')
    # part_one('scratch.txt')
    part_two('input.txt')
    # part_two('test.txt')
    # part_two('scratch.txt')


if __name__ == '__main__':
    main()
