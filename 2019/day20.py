from collections import defaultdict, deque
from my_utils import get_data


# Day 20: Donut Maze
# https://adventofcode.com/2019/day/20


def parse_donut(grid: list[str]) \
    -> list[tuple[tuple[int, int], dict[str, list[tuple[int, int]]]]]:
    donut = []
    portals = defaultdict(list)
    for r, line in enumerate(grid):
        for c, row in enumerate(line):
            if row == '.':
                donut.append((r, c))
            elif row.isalpha():
                if r + 1 < len(grid) and grid[r + 1][c].isalpha():
                    name = row + grid[r + 1][c]
                    if r + 2 < len(grid) and grid[r + 2][c] == '.':
                        portals[name].append((r + 2, c))
                    else:
                        portals[name].append((r - 1, c))
                elif c + 1 < len(line) and grid[r][c + 1].isalpha():
                    name = row + grid[r][c + 1]
                    if c + 2 < len(line) and grid[r][c + 2] == '.':
                        portals[name].append((r, c + 2))
                    else:
                        portals[name].append((r, c - 1))

    portal_counts = {key: len(portals[key]) for key in portals}
    if any(p for p in portal_counts if portal_counts[p] > 2):
        raise KeyError('Found a portal with more that 2 connections')

    return donut, portals


def get_portal_pairs(portals: dict[str, list[tuple[int, int]]]) \
    -> dict[tuple[int, int], tuple[int, int]]:
    portal_pairs = {}
    for key in portals:
        if len(portals[key]) == 2:
            portal_pairs[portals[key][0]] = portals[key][1]
            portal_pairs[portals[key][1]] = portals[key][0]

    return portal_pairs


def solve_1(data: list[str]) -> int:
    donut, portals = parse_donut(data)
    portal_pairs = get_portal_pairs(portals)
    start = portals['AA'][0]
    end = portals['ZZ'][0]
    queue = deque([(*start, 0)])
    visited = set()

    while queue:
        r, c, steps = queue.popleft()

        if (r, c) == end:
            return steps

        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r + dr, c + dc
            if (nr, nc) in visited:
                continue
            if (nr, nc) in portal_pairs:
                queue.append((*portal_pairs[(nr, nc)], steps + 2))
            elif (nr, nc) in donut:
                queue.append((nr, nc, steps + 1))
            visited.add((nr, nc))

    return -1


def solve_2(data: list[str]) -> int:
    donut, portals = parse_donut(data)
    portal_pairs = get_portal_pairs(portals)
    start = portals['AA'][0]
    end = portals['ZZ'][0]
    queue = deque([(*start, 0, 0)])
    visited = set()

    while queue:
        r, c, steps, level = queue.popleft()

        if (r, c) == end and level == 0:
            return steps

        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r + dr, c + dc
            if (nr, nc, level) in visited:
                continue
            if (nr, nc) in portal_pairs:
                if 3 < nr < len(data) - 3 and 3 < nc < len(data[4]) - 3:
                    queue.append((*portal_pairs[(nr, nc)], steps + 2, level + 1))
                elif level > 0:
                    queue.append((*portal_pairs[(nr, nc)], steps + 2, level - 1))
            elif (nr, nc) in donut:
                queue.append((nr, nc, steps + 1, level))
            visited.add((nr, nc, level))

    return -1


if __name__ == '__main__':
    data_input = get_data('inputs/20.txt')
    print(f'#1: {solve_1(data_input)}')
    # data_input = get_data('inputs/20_ex2.txt')
    print(f'#2: {solve_2(data_input)}')
