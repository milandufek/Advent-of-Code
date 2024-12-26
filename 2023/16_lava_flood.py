from collections import deque
from my_utils import get_data


# https://adventofcode.com/2023/day/16


def bfs(grid: list[str], r: int, c: int, dr: int, dc: int) -> int:
    queue = deque([(r, c, dr, dc)])
    seen = set()

    def move(r, c, dr, dc):
        if (r, c, dr, dc) not in seen:
            seen.add((r, c, dr, dc))
            queue.append((r, c, dr, dc))

    rows = len(grid)
    cols = len(grid[0])

    while queue:
        r, c, dr, dc = queue.popleft()
        r += dr
        c += dc

        if r < 0 or r >= rows or c < 0 or c >= cols:
            continue

        ch = grid[r][c]

        if ch == '.' or (ch == '-' and dc != 0) or (ch == '|' and dr != 0):
            move(r, c, dr, dc)
        elif ch == '/':
            dr, dc = -dc, -dr
            move(r, c, dr, dc)
        elif ch == '\\':
            dr, dc = dc, dr
            move(r, c, dr, dc)
        else:
            directions = [(1, 0), (-1, 0)] if ch == '|' else [(0, 1), (0, -1)]
            for dr, dc in directions:
                move(r, c, dr, dc)

    return len({(r, c) for (r, c, _, _) in seen})


def solve_1(grid: list[str]) -> int:
    return bfs(grid, 0, -1, 0, 1)


def solve_2(grid: list[str]) -> int:
    max_score = 0
    for i in range(len(grid)):
        directions = [
            (i, -1, 0, 1),
            (i, len(grid[0]), 0, -1),
            (-1, i, 1, 0),
            (len(grid), i, -1, 0)
        ]
        for r, c, dr, dc in directions:
            max_score = max(max_score, bfs(grid, r, c, dr, dc))

    return max_score


if __name__ == '__main__':
    data_input = get_data('inputs/16.in')
    print(f'Score #1: {solve_1(data_input)}')
    print(f'Score #2: {solve_2(data_input)}')
