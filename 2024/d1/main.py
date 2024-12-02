from math import ceil

filename = 'input.txt'
# filename = 'test.txt'
left_list = []
right_list = []

def init():
    with open(filename) as file:
        for line in file:
            left, right = [int(i) for i in line.split()]
            left_list.append(left)
            right_list.append(right)


def part_one():
    init()
    left_list.sort()
    right_list.sort()
    res = 0
    for i in range(len(left_list)):
        res += abs(left_list[i] - right_list[i])
    print(res)


def part_two():
    res = 0
    for left in left_list:
        occ = right_list.count(left)
        res += left * occ
    print(res)

def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()