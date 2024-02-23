from collections import defaultdict
from my_utils import get_data


# https://adventofcode.com/2021/day/12


def parse_input(_input: list) -> dict[str, list[str]]:
    edges = defaultdict(list)
    for line in _input:
        a, b = line.split('-')
        edges[a] += [b]
        edges[b] += [a]

    return edges


def count(node: str, edges: dict[str, list[str]], visited: set = None) -> int:
    if node == 'end':
        return 1

    if visited is None:
        visited = set()

    total = 0
    for edge in edges[node]:
        if edge in visited:
            continue

        total += count(edge, edges, visited | {node} if node.lower() == node else visited)

    return total


def count_2(node: str, edges: dict[str, list[str]], visited: set = None,
            second: bool = False) -> int:
    if node == 'end':
        return 1

    if visited is None:
        visited = set()

    total = 0
    for edge in edges[node]:
        if edge in visited and second or edge == 'start':
            continue

        if edge in visited:
            total += count_2(edge, edges, visited | {node} if node.lower() == node else visited, True)
        else:
            total += count_2(edge, edges, visited | {node} if node.lower() == node else visited, second)

    return total


def solve_1(_input: str) -> int:
    edges = parse_input(_input)

    return count('start', edges)


def solve_2(_input: str) -> int:
    edges = parse_input(_input)

    return count_2('start', edges)


def test_part1():
    example = get_data('inputs/12_example.in')
    example_2 = get_data('inputs/12_example_2.in')
    example_3 = get_data('inputs/12_example_3.in')
    assert solve_1(example) == 10
    assert solve_1(example_2) == 19
    assert solve_1(example_3) == 226


def test_part2():
    example_2 = get_data('inputs/12_example_2.in')
    example_3 = get_data('inputs/12_example_3.in')
    assert solve_2(example_2) == 103
    assert solve_2(example_3) == 3509


if __name__ == '__main__':
    data_input = get_data('inputs/12.in')
    print(f'Score #1: {solve_1(data_input)}')
    print(f'Score #2: {solve_2(data_input)}')
