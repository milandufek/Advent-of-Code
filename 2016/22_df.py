from typing import Iterable
from my_utils import get_data


# https://adventofcode.com/2016/day/22


class Node:
    def __init__(self, path: str, size: int, used: int, avail: int, use: int) -> None:
        self.path = path
        self.size = size
        self.used = used
        self.avail = avail
        self.use = use
        self.x = int(path.split('-')[1][1:])
        self.y = int(path.split('-')[2][1:])

    @property
    def position(self) -> tuple[int, int]:
        return self.x, self.y

    def __repr__(self) -> str:
        return f'name={self.path} pos={self.position} ' \
               f'size={self.size} used={self.used} avail={self.avail} use={self.use}'

    def __eq__(self, other: 'Node') -> bool:
        return self.position == other.position


def parse_nodes(data: list[str]) -> list:
    nodes = []
    for line in data:
        if line.startswith('/dev/'):
            path, size, used, avail, use = line.split()
            nodes.append(Node(path, int(size[:-1]), int(used[:-1]), int(avail[:-1]), int(use[:-1])))

    return nodes



def prepare_grid(nodes: list[Node]) -> dict[tuple[int, int]]:
    grid = {}
    xmax = max(node.x for node in nodes)
    ymax = max(node.y for node in nodes)
    wall_beginning = xmax

    for node in nodes:
        if node.position == (0, 0):
            grid[node.position] = 'S'
        elif node.position == (xmax, 0):
            grid[node.position] = 'G'
        elif node.used == 0:
            grid[node.position] = '_'
            empty = node.position
        elif node.size > 100:
            grid[node.position] = '#'
            wall_beginning = min(node.x, wall_beginning)
        else:
            grid[node.position] = '.'

    def print_grid(g: dict[tuple[int, int]]) -> None:
        for y in range(ymax + 1):
            row = ''
            for x in range(xmax + 1):
                row += grid.get((x, y), '')
            print(row)

    print_grid(grid)

    return empty, wall_beginning


def solve_1(data: list) -> int:
    nodes = parse_nodes(data)
    return sum(
        True for a in nodes
        for b in nodes
        if a != b and 0 < a.used <= b.avail
    )


def solve_2(data: list) -> int:
    nodes = parse_nodes(data)
    xmax = max(node.x for node in nodes)
    empty, wall_beginning = prepare_grid(nodes)
    steps = 0
    steps += empty[0] - wall_beginning + 1  # pass the wall
    steps += empty[1]                       # move to the top
    steps += xmax - wall_beginning          # move to the goal data
    steps += (xmax - 1) * 5 + 1             # move to our disk and copy the data
    return steps


if __name__ == '__main__':
    data_input = get_data('inputs/22.in')
    print(f'Part 1: {solve_1(data_input)}')
    print(f'Part 2: {solve_2(data_input)}')
