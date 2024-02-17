from collections import deque
from my_utils import get_data


# https://adventofcode.com/2023/day/10


def solve(grid: list) -> int:
    for r, row in enumerate(grid):
        if 'S' in row:
            start = r, row.index('S')
            break

    q = deque([start])
    path = {start}

    while q:
        r, c = q.popleft()
        ch = grid[r][c]

        # UP
        _next = (r - 1, c)
        if (
            r > 0 and
            ch in 'S|JL' and
            grid[r - 1][c] in '|7F' and
            _next not in path
        ):
            q.append(_next)
            path.add(_next)

        # DOWN
        _next = (r + 1, c)
        if (
            r < len(grid) - 1 and
            ch in 'S|7F' and
            grid[r + 1][c] in '|JL' and
            _next not in path
        ):
            q.append(_next)
            path.add(_next)

        # LEFT
        _next = (r, c - 1)
        if (
            c > 0 and
            ch in 'S-J7' and
            grid[r][c - 1] in '-LF' and
              _next not in path
        ):
            q.append(_next)
            path.add(_next)

        # RIGHT
        _next = (r, c + 1)
        if (
            c < len(grid[r]) - 1 and
            ch in 'S-LF' and
            grid[r][c + 1] in '-J7' and
            _next not in path
        ):
            q.append(_next)
            path.add(_next)

    print_path(grid, path)

    return len(path) // 2


def print_path(grid: list, path: set) -> None:
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            print(ch if (r, c) in path else '.', end='')
        print()


if __name__ == '__main__':
    example = get_data('inputs/10_example.in')
    data_input = get_data('inputs/10.in')
    print(f'Example #1: {solve(example)}')
    print(f'Score #1: {solve(data_input)}')
