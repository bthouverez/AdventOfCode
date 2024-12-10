import numpy as np

filename = 'input.txt'
filename = 'test.txt'
moves = {
    '^' : (-1, 0),
    '>' : (0, 1),
    'v' : (1, 0),
    '<' : (0, -1)
}
positions = list(moves.keys())
grid = []
loop_counter = 0


def count():
    res = 0
    for row in grid:
        res += row.count('X')
    return res


def gprint():
    for row in grid:
        for cell in row:
            print(cell, end='')
        print()
    print('\n')

def guard_pos():
    for row in grid:
        for move in moves.keys():
            if move in row:
                y = grid.index(row)
                x = row.index(move)
                pos = (y, x)
                return pos, move

def step():
    global loop_counter
    pos, move = guard_pos()
    grid[pos[0]][pos[1]] = 'X'


    nextpos = (pos[0] + moves[move][0], pos[1] + moves[move][1])
    if nextpos[0] < 0 or nextpos[1] < 0 or nextpos[0] >= len(grid) or nextpos[1] >= len(grid):
        grid[pos[0]][pos[1]] = 'X'
        print(pos)
        return False
    if  grid[nextpos[0]][nextpos[1]] == 'X':
        loop_counter += 1
    if  grid[nextpos[0]][nextpos[1]] == '#':
        move = positions[(positions.index(move)+1)%len(positions)]
        grid[pos[0]][pos[1]] = move
    else:
        grid[nextpos[0]][nextpos[1]] = move
    return True


def init():
    with open(filename) as file:
        for line in file:
            grid.append(list(line[:-1]))
    gprint()


def part_one():
    init()
    i = 0
    gprint()
    while step():
        i+=1
        # if i % 600 == 0:
        #     gprint()
    gprint()
    print(count())
    print(loop_counter)

def part_two():
    init()


def main():
    part_one()
    # part_two()


if __name__ == '__main__':
    main()
