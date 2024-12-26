# https://adventofcode.com/2017/day/7


def parse_input(file_name: str) -> list[str]:
    with open(file_name) as f:
        lines = f.read().splitlines()

    graph = {}
    weights = {}
    for line in lines:
        if len(line.split()) < 2:
            node, weight = line.split()
        else:
            node, weight, *children = line.split()
            children = [child.strip(',') for child in children[1:]]

        graph[node] = children
        weights[node] = int(weight.strip('()'))

    return graph, weights


def solve_1(graph: dict, *args) -> str:
    nodes = set(graph.keys())
    children = set()
    for _, child_nodes in graph.items():
        children.update(child_nodes)

    return (nodes - children).pop()


def solve_2(graph: dict, weights: dict) -> int:

    def find_weight(node: str) -> int:
        if not graph[node]:
            return weights[node]

        return weights[node] + sum(find_weight(child) for child in graph[node])

    def find_unbalanced(node: str) -> int:
        if not graph[node]:
            return weights[node]

        children_weights = [find_weight(child) for child in graph[node]]

        if len(set(children_weights)) == 1:
            return weights[node] + sum(children_weights)

        for child in graph[node]:
            if children_weights.count(find_weight(child)) == 1:
                return find_unbalanced(child)

        return 0

    root = solve_1(graph)

    return find_unbalanced(root)


if __name__ == '__main__':
    example_input = parse_input('inputs/07_example.in')
    # print(f'Part 1: {solve_1(example_input)}')
    data_input = parse_input('inputs/07.in')
    print(f'Part 1: {solve_1(*data_input)}')
    print(f'Part 2: {solve_2(*data_input)}')
