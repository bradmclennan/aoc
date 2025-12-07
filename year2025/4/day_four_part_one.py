def count_rolls(sub_grid: list[list[str]]) -> int:
    return [position for row in sub_grid for position in row].count("@")


def get_output(file):
    grid = parse_grid(file)
    return [count_rolls(sub_grid) <= 4 for sub_grid in sub_grids(grid) if sub_grid[1][1] == "@"].count(True)


def parse_grid(file) -> list[list[str]]:
    lines = open(file).read().splitlines()
    return [list(row) for row in lines]


def sub_grid_at_position(grid: list[list[str]], i: int, j: int) -> list[list[str]]:
    sub_grid = [[get_position_str(grid, l, k) for l in range(i - 1, i + 2)] for k in range(j - 1, j + 2)]
    return sub_grid


def get_position_str(grid: list[list[str]], i: int, j: int) -> str:
    try:
        if i < 0 or j < 0:
            return "."
        return grid[j][i]
    except IndexError:
        return "."


def sub_grids(grid: list[list[str]]) -> list[list[list[str]]]:
    return [sub_grid_at_position(grid, i, j) for j, row in enumerate(grid) for i, position in enumerate(row)]


if __name__ == '__main__':
    print(get_output("input.txt"))
