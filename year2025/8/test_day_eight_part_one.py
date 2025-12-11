from day_eight_part_one import get_output, graph_from_pair


def test_graph_basic():
    graph = {'1': {'1'}, '2': {'2'}, '3': {'3'}}
    graph_from_pair(graph, '1', '2')
    assert graph == {'1': {'1', '2'}, '3': {'3'}}


def test_graph_join_circuits_first():
    graph = {'1': {'1', '2'}, '3': {'3'}}
    graph_from_pair(graph, '2', '3')
    assert graph == {'1': {'1', '2', '3'}}


def test_graph_join_circuits_second():
    graph = {'1': {'1', '2'}, '3': {'3'}}
    graph_from_pair(graph, '3', '2')
    assert graph == {'1': {'1', '2', '3'}}


def test_graph_join_circuits_first_equal():
    graph = {'1': {'1', '2'}, '3': {'3', '4'}}
    graph_from_pair(graph, '2', '3')
    assert graph == {'1': {'1', '2', '3', '4'}}


def test_graph_join_circuits_second_equal():
    graph = {'1': {'1', '2'}, '3': {'3', '4'}}
    graph_from_pair(graph, '3', '2')
    assert graph == {'3': {'3', '4', '1', '2'}}


def test_get_output():
    assert get_output("test.txt", 10) == 40
