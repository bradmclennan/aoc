def get_output(file):
    banks = read_banks(file)
    return sum([max_joltage("98765"), 811111111119, 434234234278, 888911112111])


def read_banks(file) -> list[str]:
    return open(file).read().split("\n")


def max_joltage(bank) -> int:
    batteries = parse_batteries(bank)
    return int(sorted([x for x in find_joltages(batteries) if len(x) <= 12])[-1])

    # 98765
    #   9 + 8 + 7 + 6 + 5, [0,1,2,3,4]
    #   9 + 8 + 7 + 6, [0,1,2,3]
    #   9 + 8 + 7 + 5, [0,1,2,4]
    #   9 + 8 + 6 + 5, [0,1,3,4]
    #   9 + 7 + 6 + 5, [0,2,3,4]
    #   9 + 8 + 7, [0,1,2]
    #   9 + 8 + 6, [0,1,3]
    #   9 + 8 + 5, [0,1,4]
    #   9 + 7 + 6, [0,2,3]
    #   9 + 7 + 5, [0,2,4]
    #   9 + 6 + 5, [0,3,4]
    #   9 + 8, [0,1]
    #   9 + 7, [0,2]
    #   9 + 6, [0,3]
    #   9 + 5, [0,4]
    #   9, [0]

    #   8 + 7 + 6 + 5, [1,2,3,4]
    #   8 + 7 + 6, [1,2,3]
    #   8 + 7 + 5, [1,2,4]
    #   8 + 6 + 5, [1,3,4]
    #   8 + 7, [1,2]
    #   8 + 6, [1,3]
    #   8 + 5, [1,4]
    #   8, [1]

    #   7 + 6 + 5, [2,3,4]
    #   7 + 6, [2,3]
    #   7 + 5, [2,4]
    #   7, [2]

    #   6 + 5, [3,4]
    #   6, [3]

    #   5, [4]


def find_joltages(batteries: list[str]) -> list[str]:
    if not batteries: return []
    joltages = [batteries[0] + "".join(find_joltages(batteries[1:]))]
    joltages = joltages + find_joltages(batteries[1:])
    print(joltages)
    return joltages


def remaining_batteries(batteries: list[int], index) -> list[int]:
    return [y for y in batteries[index]]


def parse_batteries(line) -> list[str]:
    return [x for x in list(line)]


if __name__ == '__main__':
    print(get_output("input.txt"))
