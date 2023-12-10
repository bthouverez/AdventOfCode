filename = 'input.txt'
filename = 'test.txt'
data = []


def load():
    global data
    with open(filename) as file:
        for line in file:
            data.append([int(i) for i in line.split()])

def differences(tab):
    val = tab[0]
    diffs = []
    for ii in range(1, len(tab)):
        diffs.append(tab[ii]-val)
        val = tab[ii]
    return diffs

def main_p1():
    global data
    load()
    print(data)
    differences(data[0])


def main_p2():
    pass


if __name__ == '__main__':
    main_p1()