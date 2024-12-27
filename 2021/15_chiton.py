import heapq
from my_utils import get_data


# https://adventofcode.com/2021/day/15


def solve(data: list, part: int = 1) -> int:
    grid = get_grid(data) if part == 1 else expand_grid(data)
    rows = len(grid)
    cols = len(grid[0])
    end = (rows - 1, cols - 1)
    pq = [(0, 0, 0)]
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while pq:
        risk, r, c = heapq.heappop(pq)

        if (r, c) == end:
            return risk
        if (r, c) in visited:
            continue
        visited.add((r, c))

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue
            heapq.heappush(pq, (risk + grid[nr][nc], nr, nc))


def get_grid(data: list) -> list[list[int]]:
    return [list(map(int, list(x.strip()))) for x in data]


def print_grid(grid: list[list[int]]) -> None:
    for row in grid:
        print(''.join(map(str, row)))


def expand_grid(data: list[list[int]]) -> list[list[int]]:
    grid: list[list[int]] = [list(map(int, list(x.strip()))) for x in data]
    new_grid = []
    for i in range(5 * len(grid)):
        new_row = []
        for j in range(5 * len(grid[0])):
            origin_value = grid[i % len(grid)][j % len(grid[0])]
            increment = i // len(grid) + j // len(grid[0])
            new_value = origin_value + increment
            if new_value > 9:
                new_value = new_value % 10 + 1
            new_row.append(new_value)
        new_grid.append(new_row)

    # print_grid(new_grid)
    return new_grid


if __name__ == '__main__':
    # data_input = get_data('inputs/15_example.in')
    data_input = get_data('inputs/15.in')
    print(f'#1: {solve(data_input)}')
    print(f'#2: {solve(data_input, 2)}')
