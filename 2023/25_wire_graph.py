import networkx as nx
from utils import get_data


# https://adventofcode.com/2023/day/25


def solve(data: list) -> int:
    g = nx.Graph()

    for line in data:
        left, right = line.split(':')
        for node in right.split():
            g.add_edge(left, node)
            g.add_edge(node, left)

    g.remove_edges_from(nx.minimum_edge_cut(g))
    a, b = nx.connected_components(g)

    return len(a) * len(b)


if __name__ == '__main__':
    example = get_data('inputs/25_example.in')
    data = get_data('inputs/25.in')
    print(f'Example #1: {solve(example)}')
    print(f'Score #1: {solve(data)}')
