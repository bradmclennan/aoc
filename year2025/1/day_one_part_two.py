from functools import reduce


def count_passes(x, y):
    positions = range(min(x, y), max(x, y))[1:]
    return [position % 100 for position in positions].count(0)


def get_password(file):
    rotations = get_rotations(file)
    initial_points = [50]
    points = reduce(lambda x, y: accumulate_points(x, y), rotations, initial_points)
    print(points)
    diffs = [[x, points[i + 1]] for i, x in enumerate(points[:-1])]
    print(diffs)
    counts = [count_passes(x[0], x[1]) for x in diffs]
    print([str(diffs[i]) + "=" + str(x) for i, x in enumerate(counts)])
    return sum(counts) + [x % 100 for x in points].count(0)


def accumulate_points(points, rotation) -> list[int]:
    return points + [process_rotation(points[-1], rotation)]


def process_rotation(current_point, rotation) -> int:
    return current_point + rotation


def get_rotations(file) -> list[int]:
    return list(map(lambda x: parse_rotation(x), get_lines(file)))


def get_lines(file) -> list[str]:
    return open(file).read().splitlines()


def parse_rotation(x) -> int:
    amount = int(x[1:])
    multiplier = 1 if x[0] == 'R' else -1
    return amount * multiplier


if __name__ == '__main__':
    print(get_password("input.txt"))
