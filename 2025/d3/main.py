
def part_one(filename):
    res = 0
    with open(filename) as f:
        grid = f.read().split('\n')
        size = len(grid[0])
        print(grid)
        for i in range(size):
            for j in range(size):
                if grid[i][j] == '.':
                    continue
                # get every 8 adjacent cells
                adj = ""
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        if di == 0 and dj == 0:
                            continue
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < size and 0 <= nj < size:
                            adj += grid[ni][nj]
                if adj.count("@") < 4: res+=1
                print(f'Cell {i},{j}={grid[i][j]} Adj={adj} → {adj.count("@") < 4 and "OK" or "NOT OK"}')

    print(f'Part one: {res}')


def part_two(filename):
    res = 0
    with open(filename) as f:
        grid = f.read().split('\n')
        size = len(grid[0])
        print(grid)
        stop = False
        while not stop:
            ngrid = []
            for i in range(size):
                nline = ""
                for j in range(size):
                    if grid[i][j] == '.':
                        continue
                    # get every 8 adjacent cells
                    adj = ""
                    for di in (-1, 0, 1):
                        for dj in (-1, 0, 1):
                            if di == 0 and dj == 0:
                                continue
                            ni = i + di
                            nj = j + dj
                            if 0 <= ni < size and 0 <= nj < size:
                                adj += grid[ni][nj]
                    if adj.count("@") < 4:
                        res+=1
                        nline+='.'
                    else:
                        nline+='@'
                    print(f'Cell {i},{j}={grid[i][j]} Adj={adj} → {adj.count("@") < 4 and "OK" or "NOT OK"}')
                print(f'New line: {nline}')
                ngrid.append(nline)
            stop = ngrid == grid
            grid = ngrid
            print('Grid completed')
    print(f'Part two: {res}')




def main():
    # part_one('scratch.txt')
    # part_one('test.txt')
    # part_one('input.txt')
    # part_two('input.txt')
    # 166984328725620 too low

    part_two('test.txt')
    # part_two('scratch.txt')


if __name__ == '__main__':
    main()
