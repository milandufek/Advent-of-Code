import heapq
from my_utils import get_data


# https://adventofcode.com/2021/day/15


def solve_1(data: list):
    grid: list[list[int]] = [list(map(int, list(x.strip()))) for x in data]
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


if __name__ == '__main__':
    data_input = get_data('inputs/15.in')
    print(f'#1: {solve_1(data_input)}')
