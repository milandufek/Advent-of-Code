from my_utils import get_data


# https://adventofcode.com/2019/day/6


def get_graph(data_input: list[str]) -> dict:
    graph: dict = {}
    for line in data_input:
        inner, outer = line.strip().split(')')
        graph[outer] = inner

    return graph


def steps_to_start(graph: dict, orbit: str) -> set:
    steps = set()
    while orbit != 'COM':
        orbit = graph[orbit]
        steps.add(orbit)

    return steps


def solve_1(graph: dict) -> int:
    return sum(len(steps_to_start(graph, orbit)) for orbit in graph.keys())


def solve_2(graph: dict) -> int:
    return len((steps_to_start(graph, 'YOU') ^ steps_to_start(graph, 'SAN')))


if __name__ == '__main__':
    data_input = get_data('inputs/06.txt')
    graph: dict = get_graph(data_input)
    print(f'#1: {solve_1(graph)}')
    print(f'#2: {solve_2(graph)}')
