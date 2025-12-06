def get_output(file):
    ids = get_ids(file)
    return sum_ids(ids)


def get_ids(file):
    return open(file).read().split(",")


def sum_ids(ids) -> int:
    invalid_ids = sum([get_invalid_ids_from_str(x) for x in ids], [])
    return sum(invalid_ids)


def get_invalid_ids_from_str(id_str) -> list[int]:
    ints = parse_ints(id_str)
    return get_invalid_ids(ints[0], ints[1])


def parse_ints(range_str) -> list[int]:
    return [int(x) for x in (range_str.split("-"))]


def get_invalid_ids(start, end) -> list[int]:
    return [x for x in range(start, end + 1) if is_invalid_id(x)]


def is_invalid_id(id_num) -> bool:
    index_str = str(id_num)
    mid_index = int(len(index_str) / 2)
    equal = index_str[:mid_index] == index_str[mid_index:]
    return equal


if __name__ == '__main__':
    print(get_output("input.txt"))
