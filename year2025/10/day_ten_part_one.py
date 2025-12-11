from itertools import product
from re import search, findall


def button_presses_for_machine(machine) -> int:
    print("try machine")
    num_buttons = len(machine[1])
    print("buttons = {0}".format(num_buttons))
    for max_presses in range(1, num_buttons):
        print("max presses = {0}".format(max_presses))
        button_combinations = product(range(0, num_buttons), repeat=max_presses)
        button_combinations = [list(x) for x in button_combinations]
        sorted_combinations = sorted(button_combinations, key=lambda item: len(item))
        for buttons in sorted_combinations:
            length = try_presses(machine, buttons)
            if length > 0:
                print("success")
                return len(buttons)
    return 0


def try_presses(machine, buttons: list[int]):
    indicator = machine[0]
    all_buttons = machine[1]
    lights = [0 for _ in indicator]
    for button in buttons:
        for x in all_buttons[button]:
            lights[x] = not lights[x]
    if lights == indicator:
        return len(buttons)
    return -1


def get_output(file):
    machines = parse_machines(file)
    button_presses = fewest_button_presses_per_machine(machines)
    print(button_presses)
    return sum_button_presses(button_presses)


def fewest_button_presses_per_machine(machines: list[tuple[list[int], list[list[int]]]]) -> list[int]:
    return [button_presses_for_machine(machine) for machine in machines]


def parse_machines(file) -> list[tuple[list[int], list[list[int]]]]:
    lines = open(file).read().splitlines()
    return [parse_line(line) for line in lines]


def parse_line(line: str) -> tuple[list[int], list[list[int]]]:
    light_string = search(r"([.#]+)", line).group()
    lights = [parse_light_char(char) for char in light_string]
    buttons_string = line.split(" ")[1:-1]
    buttons = [parse_button(button) for button in buttons_string]
    return lights, buttons

def parse_button(button):
    return [int(num) for num in findall("\d+", button)]



def parse_light_char(char: str) -> int:
    if char == ".": return 0
    return 1


def sum_button_presses(button_presses) -> int:
    return sum(button_presses)


if __name__ == '__main__':
    print(get_output("input.txt"))
