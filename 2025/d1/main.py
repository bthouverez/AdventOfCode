import numpy as np


def part_one(filename):
    dial = 50
    print(dial)
    password = 0
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            side = line[0]
            value = line[1:]
            dial += side == 'L' and -int(value)%100 or int(value)%100
            dial = dial < 0 and 100 + dial or dial % 100
            if dial == 0: password+=1
            print(line[0], line[1:], '→', dial)
    print('Part one:', password)

def part_two(filename, dial):
    print(dial)
    password = 0
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            side = line[0]
            value = int(line[1:])
            roll = side == 'L' and -value or value
            if roll < 0:
                passed_0 = 5
            else:
                passed_0 = (dial + roll) // 100
            # if passed_0 < 0: passed_0 = -passed_0-1
            ndial = (dial + roll)%100
            password += passed_0
            password += 1 if dial == 0 else 0
            print(dial,': ', line, ' (', roll, ') [', passed_0 ,'] → ', ndial, sep="")
            dial = ndial
    print('Part two:', password)

def main():
    # part_two('input.txt', 50)
    # part_two('test.txt', 50)
    part_two('scratch.txt', 50)
    # part_two()1


if __name__ == '__main__':
    main()
