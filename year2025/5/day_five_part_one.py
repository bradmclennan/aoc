def get_output(file):
    file_sections = open(file).read().split("\n\n")
    fresh_ranges = parse_fresh_ranges(file_sections[0])
    ingredient_ids = parse_ingredient_ids(file_sections[1])
    ingredient_id_to_fresh = get_ingredient_id_to_fresh(ingredient_ids, fresh_ranges)
    return len([fresh for ingredient_id, fresh in ingredient_id_to_fresh.items() if fresh])


def parse_fresh_ranges(ranges_str) -> list[list[int]]:
    lines = ranges_str.splitlines()
    return [[int(id_str) for id_str in line.split("-")] for line in lines]


def get_ingredient_id_to_fresh(ingredient_ids, fresh_ranges) -> dict[int, bool]:
    id_dict = {ingredient_id: False for index, ingredient_id in enumerate(ingredient_ids)}
    id_dict = {ingredient_id: is_fresh(fresh_ranges, id_dict, ingredient_id) for index, ingredient_id in enumerate(ingredient_ids)}
    return id_dict


def is_fresh(fresh_ranges: list[list[int]], id_dict: dict[int, bool], ingredient_id) -> bool:
    return id_dict[ingredient_id] or any(in_fresh_range(ingredient_id, fresh_range) for fresh_range in fresh_ranges)


def in_fresh_range(ingredient_id, fresh_range) -> bool:
    return ingredient_id in range(fresh_range[0], fresh_range[1] + 1)


def parse_ingredient_ids(ingredients_str) -> list[int]:
    return [int(ingredient_id_str) for ingredient_id_str in ingredients_str.splitlines()]


if __name__ == '__main__':
    print(get_output("input.txt"))
