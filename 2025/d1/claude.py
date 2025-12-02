def parse_rotation(line):
    """Parse une ligne de rotation (ex: 'L68' ou 'R48')"""
    direction = line[0]
    distance = int(line[1:])
    return direction, distance


def part1(rotations):
    """
    Partie 1: Compte combien de fois le cadran pointe sur 0
    à la FIN d'une rotation
    """
    position = 50
    count = 0

    for direction, distance in rotations:
        if direction == 'L':
            position = (position - distance) % 100
        else:  # direction == 'R'
            position = (position + distance) % 100

        if position == 0:
            count += 1

    return count


def part2(rotations):
    """
    Partie 2: Compte combien de fois le cadran pointe sur 0
    pendant ET à la fin des rotations (chaque clic)
    """
    position = 50
    count = 0

    for direction, distance in rotations:
        # Pour chaque clic de la rotation
        for _ in range(distance):
            if direction == 'L':
                position = (position - 1) % 100
            else:  # direction == 'R'
                position = (position + 1) % 100

            if position == 0:
                count += 1

    return count


# Lecture du fichier d'entrée
def solve(input_text):
    """Résout les deux parties du puzzle"""
    lines = input_text.strip().split('\n')
    rotations = [parse_rotation(line) for line in lines]

    password1 = part1(rotations)
    password2 = part2(rotations)

    return password1, password2

with open('input.txt', 'r') as f:
    input_text = f.read()
    password1, password2 = solve(input_text)
    print(f"Partie 1: {password1}")
    print(f"Partie 2: {password2}")