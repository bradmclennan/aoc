def get_output(file):
    manifold = open(file).read()
    manifold = manifold.replace("\n\n", "").strip()
    manifold = [list(line.strip()) for line in manifold.splitlines() if line]
    print()
    # print("before" + str(manifold))
    analyze_manifold(manifold, start_position(manifold))
    # print("after")
    # for x in manifold:
    #     print([y for y in x])
    splitters = find_splitters(manifold)
    return count_splits(manifold, splitters)


def start_position(manifold) -> list[int]:
    return [manifold[0].index("S"), 0]


def analyze_manifold(manifold, start):
    i = start[0]
    j = start[1]
    # print("analyzing " + str(i) + "," + str(j))
    # print(len(manifold))
    # print(len(manifold[0]))
    # print(manifold)
    if len(manifold) <= j or len(manifold[0]) <= i:
        return
    # print(i)
    # print(j)
    current_char = manifold[j][i]
    if current_char == "|":
        return
    if current_char == "^":
        analyze_manifold(manifold, [i - 1, j])
        analyze_manifold(manifold, [i + 1, j])
    else:
        if current_char == ".":
            manifold[j][i] = "|"
        analyze_manifold(manifold, [i, j + 1])


def find_splitters(manifold) -> list[list[int]]:
    return [[i, j] for j, row in enumerate(manifold) for i, character in enumerate(row) if character == "^"]


def count_splits(manifold, splitters) -> int:
    return [char_above_splitter(manifold, splitter) for splitter in splitters].count("|")


def char_above_splitter(manifold, splitter: list[int]) -> str:
    row = splitter[1] - 1
    col = splitter[0]
    char = manifold[row][col]
    return char


if __name__ == '__main__':
    print(get_output("input.txt"))
