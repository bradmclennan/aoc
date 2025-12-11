import math


#
def get_output(file, limit: int):
    junction_boxes = open(file).read().splitlines()
    circuits = group_junction_boxes(junction_boxes, limit)
    circuit_sizes = get_circuit_sizes(circuits)
    circuit_sizes = largest_circuit_sizes(circuit_sizes)
    return math.prod(circuit_sizes)


def get_circuit_sizes(circuits: list[list[str]]) -> list[int]:
    circuit_sizes = [count_circuit_junction_boxes(circuit) for circuit in circuits]
    circuit_sizes = sorted(circuit_sizes, reverse=True)
    print(circuit_sizes)
    return circuit_sizes


def group_junction_boxes(junction_boxes: list[str], limit: int) -> list[list[str]]:
    pairs = shortest_pairs(junction_boxes)
    print(pairs)
    graph = graph_from_pairs(pairs, limit)
    print(graph)
    clusters = get_clusters(graph)
    return clusters


def get_clusters(graph: dict[str, set[str]]) -> list[list[str]]:
    clusters = set([frozenset(value) for value in graph.values()])
    clusters = [list(x) for x in clusters]
    print("[")
    for c in clusters:
        print(" [", [b for b in c], "]")
    print("]")
    return clusters


def shortest_pairs(junction_boxes: list[str]) -> list[tuple[str, str]]:
    print("getting shortest pairs")
    pair_distances = [pair_distances_for_box(box, junction_boxes) for box in junction_boxes]
    print("filtering")
    pair_distances2 = [p for pp in pair_distances for p in pp if p[2] > 0.0]
    print("sorting pairs")
    sorted_pairs = [sort_pair(pair) for pair in pair_distances2]
    print("removing duplicate pairs")
    unique_pairs = list(set(sorted_pairs))
    print("sorting by distance")
    sorted_by_distance = sorted(unique_pairs, key=lambda item: item[2])
    return [(pair_distance[0], pair_distance[1]) for pair_distance in sorted_by_distance]


def sort_pair(pair: tuple[str, str, float]) -> tuple[str, str, float]:
    sorted_pair = sorted([pair[0], pair[1]])
    return sorted_pair[0], sorted_pair[1], pair[2]


def pair_distances_for_box(box: str, junction_boxes: list[str]) -> list[tuple[str, str, float]]:
    return [(box, b, distance(b, box)) for b in junction_boxes]


def distance(vector_str_1: str, vector_str_2: str) -> float:
    v1 = parse_vector(vector_str_1)
    v2 = parse_vector(vector_str_2)
    return math.dist(v1, v2)


def parse_vector(a: str) -> list[int]:
    return [int(char) for char in a.split(",")]


def pair_in_graph(graph, pair):
    for circuit in graph.values():
        if pair[0] in circuit and pair[1] in circuit:
            return True
    return False


def graph_from_pairs(pairs: list[tuple[str, str]], limit: int) -> dict[str, set[str]]:
    graph: dict[str, set[str]] = {}
    for p in pairs:
        graph[p[0]] = {p[0]}
        graph[p[1]] = {p[1]}
    count = 0
    for pair in pairs:
        if count == limit:
            break
        graph_from_pair(graph, pair[0], pair[1])
        clusters = get_clusters(graph)
        get_circuit_sizes(clusters)
        count = count + 1
    return graph


def graph_from_pair(graph: dict[str, set[str]], first: str, second: str):
    first_circuit = ('', 0)
    second_circuit = ('', 0)
    for key, circuit in graph.items():
        if first in circuit:
            first_circuit = (key, len(circuit))
        if second in circuit:
            second_circuit = (key, len(circuit))
    if first_circuit[0] == second_circuit[0]:
        return
    graph_from_pair_circuits(graph, first_circuit, second_circuit)


def graph_from_pair_circuits(graph: dict[str, set[str]], first_circuit: tuple[str, int],
                             second_circuit: tuple[str, int]):
    first_circuit_key = first_circuit[0]
    second_circuit_key = second_circuit[0]
    if first_circuit[1] >= second_circuit[1]:
        if second_circuit_key in graph:
            graph[first_circuit_key] = graph[first_circuit_key].union(graph[second_circuit_key])
        if second_circuit_key in graph:
            graph.pop(second_circuit_key)
    else:
        if first_circuit_key in graph:
            graph[second_circuit_key] = graph[second_circuit_key].union(graph[first_circuit_key])
        if first_circuit_key in graph:
            graph.pop(first_circuit_key)


def count_circuit_junction_boxes(circuit: list[str]) -> int:
    return len(circuit)


def largest_circuit_sizes(circuits) -> list[int]:
    return sorted(circuits)[-3:]


if __name__ == '__main__':
    print(get_output("input.txt", 1000))
