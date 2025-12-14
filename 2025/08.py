from collections import Counter
from functools import reduce
from itertools import combinations
from operator import mul
from my_utils import get_data


# https://adventofcode.com/2025/day/8


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)

        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px

        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

        return True

    def get_circuit_sizes(self) -> list[int]:
        roots = [self.find(i) for i in range(len(self.parent))]
        counts = Counter(roots)

        return sorted(counts.values(), reverse=True)


def distance_squared(p1: tuple, p2: tuple) -> int:
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2


def solve_1(data: list[str], num_connections: int = 1000) -> int:
    points = []
    for line in data:
        x, y, z = map(int, line.split(','))
        points.append((x, y, z))

    n = len(points)

    distances = [
        (distance_squared(points[i], points[j]), i, j)
        for i, j in combinations(range(n), 2)
    ]

    distances.sort()
    uf = UnionFind(n)

    for k in range(min(num_connections, len(distances))):
        _, i, j = distances[k]
        uf.union(i, j)

    sizes = uf.get_circuit_sizes()

    return reduce(mul, sizes[:3])


if __name__ == '__main__':
    example = get_data('inputs/08_example.in')
    data_input = get_data('inputs/08.in')
    print(f'Example #1: {solve_1(example, 10)}')
    print(f'Score   #1: {solve_1(data_input, 1000)}')
    # print(f'Example #2: {solve_2(example)}')
    # print(f'Score   #2: {solve_2(data_input)}')
