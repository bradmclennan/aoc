def pairs_from_points(points):
    pairs = []
    for point1 in points:
        for point2 in points:
            pairs.append((point1, point2))
    return pairs


def get_output(file):
    points = parse_points(file)
    pairs = pairs_from_points(points)
    areas = calc_areas(pairs)
    return largest_area(areas)


def parse_points(file) -> list[tuple[int, int]]:
    lines = open(file).read().splitlines()
    return [parse_point(line) for line in lines]


def parse_point(line: str) -> tuple[int, int]:
    numbers = line.split(",")
    return (int(numbers[0]), int(numbers[1]))


def calc_area(tile1: tuple[int, int], tile2: tuple[int, int]):
    return (abs(tile1[0] - tile2[0]) + 1) * (abs(tile1[1] - tile2[1]) + 1)


def calc_areas(pairs: list[tuple[tuple[int, int], tuple[int, int]]]) -> list[int]:
    return [calc_area(pair[0], pair[1]) for pair in pairs]


def largest_area(areas) -> int:
    return sorted(areas)[-1]


if __name__ == '__main__':
    print(get_output("input.txt"))
