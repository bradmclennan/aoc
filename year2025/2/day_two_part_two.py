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


# for every string count the repeats
# e.g. 1212121212
# len = 10
# for each divisor of 10? 10, 5
# is 1 repeated 10 times? no
# is 12 repeated 5 times? yes
# is 5 divisible by 2? no

# e.g. 123123123
# len = 9
# for each divisor of 9? 9, 3
# is 1 repeated 9 times? no
# is 123 repeated 3 times? yes

# e.g. 12341234
# len = 8
# for each divisor of 8? 8, 4, 2
# is str[:len/x] repeated x times?
# is 1 repeated 8 times? no
# is 12 repeated 4 times? no
# is 1234 repeated 2 times? yes

# e.g. 1111111
# len = 7
# for each divisor of 7? 7
# is 1 repeated 7 times? yes

def is_repeated_times(id_str, times) -> bool:
    length = len(id_str)
    sequence_end = int(length / times)
    return id_str.count(id_str[:sequence_end]) == times


def get_factors(num):
    return [x for x in range(2, num + 1) if num % x == 0]


def is_invalid_id(id_num) -> bool:
    id_str = str(id_num)
    length = len(id_str)
    return True if [x for x in get_factors(length) if is_repeated_times(id_str, x)] else False


if __name__ == '__main__':
    print(get_output("input.txt"))
