from my_utils import get_data


# https://adventofcode.com/2018/day/18


def print_grid(grid: list[list[str]]) -> None:
    print('---')
    for row in grid:
        print(''.join(row))


def get_adjacent(grid: list[list[str]], row: int, col: int) -> list[str]:
    rows = len(grid)
    cols = len(grid[0])
    adj = []
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if r == row and c == col:
                continue
            if r < 0 or r >= rows or c < 0 or c >= cols:
                continue
            adj.append(grid[r][c])

    return adj


def solve_1(data: list[str]) -> int:
    rows = len(data)
    cols = len(data[0])
    grid = [list(row) for row in data]
    for _ in range(10):
        new_grid = [['.' for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '.':
                    if get_adjacent(grid, r, c).count('|') >= 3:
                        new_grid[r][c] = '|'
                elif grid[r][c] == '|':
                    if get_adjacent(grid, r, c).count('#') >= 3:
                        new_grid[r][c] = '#'
                    else:
                        new_grid[r][c] = '|'
                elif grid[r][c] == '#':
                    if get_adjacent(grid, r, c).count('#') >= 1 and get_adjacent(grid, r, c).count('|') >= 1:
                        new_grid[r][c] = '#'
        # print_grid(new_grid)
        grid = new_grid

    return sum(r.count('|') for r in grid) * sum(r.count('#') for r in grid)


def solve_2(data: list[str]) -> int:
    rows = len(data)
    cols = len(data[0])
    grid = [list(row) for row in data]
    seen = []
    fingerprint = ''
    target_times = 1_000_000_000
    for i in range(target_times):
        new_grid = [['.' for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '.':
                    if get_adjacent(grid, r, c).count('|') >= 3:
                        new_grid[r][c] = '|'
                elif grid[r][c] == '|':
                    if get_adjacent(grid, r, c).count('#') >= 3:
                        new_grid[r][c] = '#'
                    else:
                        new_grid[r][c] = '|'
                elif grid[r][c] == '#':
                    adjacent = get_adjacent(grid, r, c)
                    if adjacent.count('#') >= 1 and adjacent.count('|') >= 1:
                        new_grid[r][c] = '#'

        fingerprint = ''.join(''.join(row) for row in new_grid)

        if fingerprint in seen:
            cycle_start = seen.index(fingerprint)
            cycle_length = i - cycle_start
            remaining = target_times - i
            cycle_index = cycle_start + (remaining % cycle_length) - 1
            fingerprint = seen[cycle_index]
            break

        seen.append(fingerprint)
        grid = new_grid

    return sum(r.count('|') for r in fingerprint) * sum(r.count('#') for r in fingerprint)


if __name__ == '__main__':
    # data_input = get_data('inputs/18_example.in')
    data_input = get_data('inputs/18.in')
    print(f'Part 1: {solve_1(data_input)}')
    print(f'Part 2: {solve_2(data_input)}')
