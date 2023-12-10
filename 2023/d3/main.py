filename = 'input.txt'
filename = 'test.txt'
grid = []


def loadGrid():
    with open(filename) as file:
        for line in file:
            grid.append(line)

def findNumbers2():
    numbers = []
    for line in grid:
        tab = [e for e in line.split('.') if len(e) > 1]
        for i in range(len(tab)):
            e = tab[i]
            if not e[0].isdigit(): tab[i] = e[1:]
            if not e[-1].isdigit(): tab[i] = e[:-1]
        print(tab)

def findNumbers():
    result = []
    ii = 0
    for line in grid:
        jj = 0
        tab = []
        while jj < len(line):
            # print('jj debut', jj)
            if line[jj].isdigit():
                number, length = getWholeNumber(jj, ii)
                jj += length
                tab.append(number)
            # print('jj fin', jj)
            jj += 1
        result.append(tab)
        ii+=1
    return result

# trouve le nombre entier trouvé a partir d'une case, le renvoie et sa longueur
def getWholeNumber(x, y):
    res = ""
    while grid[y][x].isdigit():
        res += grid[y][x]
        x+=1
    if res != "":
        return int(res), len(res)
    else:
        return 0,0



def getCellsAroundRectangle(x, y, w, h):
    res = grid[y - 1][x - 1:x + w + 1]
    res += grid[y + h][x - 1:x + w + 1]
    for i in range(h):
        line = grid[y + i][x - 1:x + w + 1]
        res += line[0] + line[-1]
    return res


if __name__ == '__main__':
    SOMME = 0
    loadGrid()
    numbers = findNumbers()
    nline = 0
    for tabline in numbers:
        for number in tabline:
            # print('number', number)
            startsAt = grid[nline].find(str(number))
            # print('startsAt', startsAt)
            cells = getCellsAroundRectangle(startsAt, nline, len(str(number)), 1)
            # print('cells ', cells)
            hasSymbols = False
            for e in cells.replace('.', ''):
                if not e.isalnum():
                    hasSymbols = True
            if hasSymbols:
                SOMME += number

        nline+=1
    print(SOMME)
