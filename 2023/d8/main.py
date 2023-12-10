filename = 'input.txt'
# filename = 'testp2.txt'
# filename = 'test.txt'

instructions = ""
nodes = {}

def load():
    global instructions, nodes
    with open(filename) as file:
        instructions = file.readline()[:-1]
        file.readline()
        for line in file.readlines():
            start = line.split(' = ')[0]
            end = line.split('=')[1][:-1][2:-1].split(', ')
            nodes[start] = end

def get_instruction(cpt):
    global instructions
    return 0 if instructions[cpt%len(instructions)] == 'L' else 1


def end(nodes):
    finals = [n for n in nodes if n[-1] == 'Z']
    return len(finals) == len(nodes)


def main():
    global instructions, nodes
    load()
    current = 'AAA'
    cpt = 0
    print(nodes)
    while current != 'ZZZ':
        current = nodes[current][get_instruction(cpt)]
        cpt+=1
    print(cpt)


def main_p2():
    global instructions, nodes
    load()
    cpt = 0
    currents = [n for n in nodes.keys() if n[-1] == 'A']
    print(currents)
    while not end(currents):
        n_currents = []
        leftright = get_instruction(cpt)
        for node in currents:
            n_currents.append(nodes[node][leftright])
        currents = n_currents
        cpt += 1
        # print(leftright, currents)
        if cpt % 1000000 == 0: print(cpt)
    print(cpt)


if __name__ == '__main__':
    main_p2()