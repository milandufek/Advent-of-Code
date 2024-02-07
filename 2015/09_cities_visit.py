from collections import defaultdict
from itertools import permutations
from utils import get_data


def solve(file: str = 'inputs/09.in'):
    cities = set()
    graph = defaultdict(dict)

    for line in get_data(file):
        src, _, dst, _, dist = line.split()
        cities.add(src)
        cities.add(dst)
        graph[src][dst] = int(dist)
        graph[dst][src] = int(dist)

    paths = []
    for route in permutations(cities):
        total = sum(graph[x][y] for x, y in zip(route, route[1:]))
        # total = sum(map(lambda x, y: graph[x][y], route, route[1:]))
        paths.append(total)

    print(f'Min: {min(paths)}')
    print(f'Max: {max(paths)}')


if __name__ == '__main__':
    solve()
