import math


def get_output(file):
    problems = parse_problems(file)
    answers = get_answers(problems)
    return grand_total(answers)


def get_answers(problems) -> list[int]:
    return [get_answer(problem[0], problem[1]) for problem in problems]


def parse_problems(file) -> list[list[list[int] | str]]:
    lines = open(file).read().splitlines()
    operators = parse_operators(lines[-1])
    number_grid = parse_number_grid(lines[:-1])
    return [parse_problem_at_index(index, number_grid, operators) for index, _ in enumerate(number_grid[0])]


def parse_number_grid(lines) -> list[list[int]]:
    return [parse_number_grid_row(row) for row in lines]


def parse_number_grid_row(line) -> list[int]:
    return [int(number_str) for number_str in line.split(" ") if not number_str == ""]


def parse_operators(line) -> list[str]:
    return list(line.replace(" ", ""))


def parse_problem_at_index(index: int, number_grid: list[list[int]], operators: list[str]) -> list[list[int] | str]:
    numbers = [row[index] for row in number_grid]
    problem = [numbers, operators[index]]
    return problem


def get_answer(numbers, operation) -> int:
    return math.prod(numbers) if operation == "*" else sum(numbers)


def grand_total(answers) -> int:
    return sum(answers)


if __name__ == '__main__':
    print(get_output("input.txt"))
