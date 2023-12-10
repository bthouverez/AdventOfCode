from math import ceil

filename = 'input.txt'
# filename = 'test.txt'
grid = []


def calcScore(found):
    if found == 0:
        return 0
    elif found == 1:
        return 1
    else:
        return 2*calcScore(found-1)


def findMatches(winning, user):
    res = 0
    for n in user:
        if n in winning:
            res += 1
    return res


def extractNumbers(line):
    card = line.split(':')[1]
    card = card.split('|')
    winning_numbers = card[0].split()
    user_numbers = card[1].split()
    return winning_numbers, user_numbers


def main():
    cptCard = 1
    res = 0
    with open(filename) as file:
        lines = file.readlines()
        TAB = [1]*len(lines)

        for line in lines:
            print(TAB, end=" => ")
            numberOfCards = TAB.pop(0)
            print(numberOfCards, end=" ")
            res += numberOfCards
            print(line.split(':')[0], end=", ")
            winning_numbers, user_numbers = extractNumbers(line)
            found = findMatches(winning_numbers, user_numbers)
            print('found', found, end=", ")
            for i in range(found):
                TAB[i] += numberOfCards
            print(TAB)
    print(res)


if __name__ == '__main__':
    main()