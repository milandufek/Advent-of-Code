from my_utils import get_data


# https://adventofcode.com/2025/day/4


def get_adjacent_at(grid: list[list[str]] | list[str], row: int, col: int) -> list[str]:
    rows = len(grid)
    cols = len(grid[0])
    adj = []
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if r == row and c == col:
                continue
            if r < 0 or r >= rows or c < 0 or c >= cols:
                continue
            if grid[r][c] == '@':
                adj.append(grid[r][c])
    return adj


def solve_1(grid: list[str]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue
            adj = get_adjacent_at(grid, r, c)
            count += 1 if len(adj) < 4 else 0

    return count


def solve_2(grid: list[str]) -> int:
    current_grid = [list(row) for row in grid]
    new_grid = [row.copy() for row in current_grid]
    rows = len(current_grid)
    cols = len(current_grid[0])
    count = 0
    while True:
        last_count = count
        for r in range(rows):
            for c in range(cols):
                if current_grid[r][c] != '@':
                    continue
                adj = get_adjacent_at(current_grid, r, c)
                if len(adj) < 4:
                    new_grid[r][c] = 'x'
                    count += 1

        if count == last_count:
            break

        current_grid = [row.copy() for row in new_grid]
        count = 0

    count_papers = sum(1 for row in current_grid for cell in row if cell == 'x')
    # print('\n'.join(''.join(row) for row in current_grid))

    return count_papers



if __name__ == '__main__':
    example = get_data('inputs/04_example.in')
    data_input = get_data('inputs/04.in')
    print(f'Example #1: {solve_1(example)}')
    print(f'Score   #1: {solve_1(data_input)}')
    print(f'Example #2: {solve_2(example)}')
    print(f'Score   #2: {solve_2(data_input)}')
