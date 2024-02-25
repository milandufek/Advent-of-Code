from collections import deque
import math
from my_utils import get_data


# https://adventofcode.com/2021/day/09


def check_adjacent_is_lower(grid: list[list[int]], r: int, c: int) -> bool:
    for nr in range(r - 1, r + 2):
        for nc in range(c - 1, c + 2):
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]):
                if grid[nr][nc] < grid[r][c]:
                    return False

    return True


def find_lowest_points(grid: list[list[int]]) -> list[tuple[int, int, int]]:
    lowest_points = set()
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if check_adjacent_is_lower(grid, r, c):
                lowest_points.add((r, c, col))

    return list(lowest_points)


def solve_1(_input: list[list[str]]) -> int:
    grid = [list(map(int, line)) for line in _input]
    lowest_points = find_lowest_points(grid)

    return sum(p[-1] + 1 for p in lowest_points)


def find_basin(grid: list[list[int]],
               lowest_point: tuple[int, int, int]) -> list[tuple[int, int]]:
    visited = set()
    queue = deque([lowest_point])

    while queue:
        r, c, _ = queue.popleft()

        if (r, c) in visited:
            continue

        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if (
                0 <= nr < len(grid)
                and 0 <= nc < len(grid[0])
                and grid[nr][nc] < 9
            ):
                queue.append((nr, nc, grid[nr][nc]))
                visited.add((r, c))

    return list(visited)


def solve_2(_input: list[str]) -> int:
    grid = [list(map(int, line)) for line in _input]
    lowest_points = find_lowest_points(grid)
    basins = [find_basin(grid, lp) for lp in lowest_points]
    basins.sort(key=len, reverse=True)
    top_three = [len(b) for b in basins[:3]]

    return math.prod(top_three)


if __name__ == '__main__':
    example = get_data('inputs/09_example.in')
    data_input = get_data('inputs/09.in')
    print(f'Example #1: {solve_1(example)}')
    print(f'Score #1: {solve_1(data_input)}')
    print(f'Example #2: {solve_2(example)}')
    print(f'Score #2: {solve_2(data_input)}')
