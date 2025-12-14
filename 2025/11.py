from my_utils import get_data


# https://adventofcode.com/2025/day/11


def solve_1(data: list[str]) -> int:
    graph = {}
    for line in data:
        parts = line.split()
        key = parts[0].strip(':')
        graph[key] = parts[1:]

    def dfs(node: str) -> int:
        if node == 'out':
            return 1
        else:
            return sum(dfs(x) for x in graph[node])

    return dfs('you')


if __name__ == '__main__':
    example = get_data('inputs/11_example.in')
    data_input = get_data('inputs/11.in')
    print(f'Example #1: {solve_1(example)}')
    print(f'Score   #1: {solve_1(data_input)}')
    # print(f'Example #2: {solve_2(example)}')
    # print(f'Score   #2: {solve_2(data_input)}')
