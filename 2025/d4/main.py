
def part_one(filename):
    res = 0
    with open(filename) as f:
        for line in f:
            tabline = [int(i) for i in list(line.strip())]
            battery1 = max(tabline[:-1])
            i_battery1 = tabline.index(battery1)
            battery2 = max(tabline[i_battery1+1:])
            joltage = battery1 * 10 + battery2
            print(f'{line} → {joltage}')
            res+=joltage
    print(f'Part one: {res}')


def find_max_and_truncate(bank):
    tabline = [int(i) for i in list(bank)]
    if len(bank) <= 12:
        return int(bank[0]), bank[1:]
    else:
        batteryMax = max(tabline[:-11])
    i_batteryMax = tabline.index(batteryMax)
    return batteryMax, bank[i_batteryMax+1:]

def part_two(filename):
    with open(filename) as f:
        for line in f:
            res = []
            bank = line.strip()
            while True:
                bmax, nbank = find_max_and_truncate(bank)
                if len(bank)-len(res) <= 12:
                    break
                bank = nbank
                res.append(bmax)
            print(f'Before: {bank}')
            print(*res, sep="", end=f" ({str(len(res))})\n")
'''
987654321111111
811111111111119
234234234234278
818181911112111

987654321111
811111111119
434234234278
888911112111

987654321111(12)
811111111111(12)
423423423427(12)
881819111121(12)
'''
def part_two2(filename):
    res = 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            tabline = [int(i) for i in list(line)]
            battery1 = max(tabline[:-11])
            i_battery1 = tabline.index(battery1)
            bank = line[i_battery1+1:]
            print(f'Starting bank: {battery1}{bank} (len={len(bank)})')
            batteryToRemove = 1
            while True:
                nbank = bank.replace(str(batteryToRemove), '')
                if len(nbank) < 12:
                    break
                bank = nbank
                batteryToRemove += 1
            print(f'BEFORE {battery1}{bank} → {len(bank.strip())+1}')
            print(f'To remove {batteryToRemove}')
            # bank = bank[::-1]
            while len(bank) >= 12:
                bank = bank.replace(str(batteryToRemove), '', 1)
            # bank = str(battery1)+bank[::-1]
            print(f'AFTER {battery1}{bank} → {len(bank.strip())+1}\n')
            res += int(str(battery1)+bank)

    print(f'Part two: {res}')



def main():
    # part_one('input.txt')
    # part_one('test.txt')
    # part_one('scratch.txt')
    # part_two('input.txt')
    # 166984328725620 too low

    part_two('test.txt')
    # part_two('scratch.txt')


if __name__ == '__main__':
    main()
