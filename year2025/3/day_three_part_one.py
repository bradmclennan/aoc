def get_output(file):
    banks = read_banks(file)
    return sum([max_joltage(bank) for bank in banks])


def read_banks(file) -> list[str]:
    return open(file).read().split("\n")


def max_joltage(bank) -> int:
    batteries = parse_batteries(bank)
    return int(sorted(find_joltages(batteries))[-1])


def find_joltages(batteries) -> list[str]:
    if not batteries: return []
    joltages = [batteries[0] + battery for battery in batteries[1:]]
    return joltages + find_joltages(batteries[1:])


def remaining_batteries(batteries: list[int], index) -> list[int]:
    return [y for y in batteries[index]]


def parse_batteries(line) -> list[str]:
    return [x for x in list(line)]


if __name__ == '__main__':
    print(get_output("input.txt"))
