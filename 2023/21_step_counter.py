from collections import deque
from my_utils import get_data


# https://adventofcode.com/2023/day/21


def solve_1(grid: list[str], step: int) -> int:
    start = next((c, r) for r, row in enumerate(grid)
                  for c, col in enumerate(row) if col == 'S')

    queue = deque([(*start, step)])
    seen = set()
    options = set()

    while queue:
        r, c, step = queue.popleft()

        if (r, c) in seen:
            continue

        if step % 2 == 0:
            options.add((r, c))

        if step == 0:
            continue

        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != '#':
                queue.append((nr, nc, step - 1))
                seen.add((r, c))

    return len(options)


def test_solve_1():
    example = get_data('inputs/21_example.in')
    assert solve_1(example, 6) == 16
    data_input = get_data('inputs/21.in')
    assert solve_1(data_input, 64) == 3841


if __name__ == '__main__':
    data_input = get_data('inputs/21.in')
    print(f'Score #1: {solve_1(data_input, 64)}')
