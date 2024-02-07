import numpy as np
import networkx as nx


# https://adventofcode.com/2022/day/12

def load_data(file: str = 'inputs/12.in') -> np.ndarray:
    return np.genfromtxt(file, delimiter=1, dtype=str)


def char_to_value(char: str) -> int:
    if char == 'S':
        return char_to_value('a')
    elif char == 'E':
        return char_to_value('z')
    return ord(char) - 97


def get_neighbor_edges(x: int, y: int, area: list) -> list:
    edges = []
    row_length = len(area[0])
    current_node = (x, y)
    current_value = char_to_value(area[y][x])

    # add only possible edges with value at most current + 1
    # left
    if x > 0 and char_to_value(area[y][x - 1]) <= current_value + 1:
        edges.append([current_node, (x - 1, y)])
    # right
    if x < row_length - 1 and char_to_value(area[y][x + 1]) <= current_value + 1:
        edges.append([current_node, (x + 1, y)])
    # up
    if y > 0 and char_to_value(area[y - 1][x]) <= current_value + 1:
        edges.append([current_node, (x, y - 1)])
    # down
    if y < len(area) - 1 and char_to_value(area[y + 1][x]) <= current_value + 1:
        edges.append([current_node, (x, y + 1)])

    return edges


def get_node(area: np.ndarray, char: str) -> int:
    node = np.where(area == char)
    return int(node[1]), int(node[0])


def get_nodes(area: np.ndarray, char: str) -> list:
    nodes = []
    results = np.where(area == char)

    for i in range(0, len(results[0])):
        nodes.append((int(results[1][i]), int(results[0][i])))
    return nodes


def show_shortest_path(data_file: str) -> None:
    area = load_data(data_file)
    start = get_node(area, 'S')
    dest = get_node(area, 'E')
    graph = nx.DiGraph()

    for y, line in enumerate(area):
        for x, _ in enumerate(line):
            edges = get_neighbor_edges(x, y, area)
            for edge in edges:
                graph.add_edge(edge[0], edge[1])

    length = nx.shortest_path_length(graph, source=start, target=dest)
    print(f'#1 for {data_file}: {length}')

    lengths = set()
    start_nodes = get_nodes(area, 'a')
    start_nodes.append(start)

    for node in start_nodes:
        try:
            lengths.add(nx.shortest_path_length(graph, source=node, target=dest))
        except nx.exception.NetworkXNoPath:
            pass

    print(f'#2 for {data_file}: {min(lengths)}')


if __name__ == '__main__':
    show_shortest_path('inputs/12_example.in')
    show_shortest_path('inputs/12.in')
