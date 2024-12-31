# https://adventofcode.com/2024/day/15


def parse_input(path: str) -> tuple[list[str], str]:
    with open(path) as f:
        raw_grid, moves = f.read().strip().split('\n\n')
        grid = raw_grid.split('\n')
        moves = ''.join(moves.split('\n'))
    return grid, moves

def get_start(grid: list[list[str]]) -> tuple[int, int]:
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '@':
                return r, c
    return -1, -1

def expand_grid(grid: list[list[str]]) -> list[list[str]]:
    expanded_chars = {
        '#': '##',
        'O': '[]',
        '.': '..',
        '@': '@.',
    }
    expanded_grid = []
    for row in grid:
        expanded_row = []
        for char in row:
            expanded_row.extend(expanded_chars[char])
        expanded_grid.append(expanded_row)
    return expanded_grid

def print_grid(grid: list[list[str]]):
    for row in grid:
        print(''.join(row))

def get_score(grid: list[list[str]]):
    score = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '[':
                score += r * 100 + c
    return score

def solve(input_file: str) -> int:
    grid, moves = parse_input(input_file)
    grid = expand_grid(grid)
    position = get_start(grid)
    direction_map = {
        '^': [-1, 0],
        'v': [1, 0],
        '>': [0, 1],
        '<': [0, -1],
    }

    def swap(tile_a: tuple[int, int], tile_b: tuple[int, int]) -> None:
        r1, c1 = tile_a
        r2, c2 = tile_b
        grid[r1][c1], grid[r2][c2] = grid[r2][c2], grid[r1][c1]

    for move in moves:
        dr, dc = direction_map[move]
        movable = [position]
        can_move = True
        for r, c in movable:
            nr, nc = r + dr, c + dc
            if (nr, nc) in movable:
                continue
            tile = grid[nr][nc]
            if tile == '#':
                can_move = False
                break
            if tile == '[':
                movable.append((nr, nc))
                movable.append((nr, nc + 1))
            elif tile == ']':
                movable.append((nr, nc))
                movable.append((nr, nc - 1))

        if can_move:
            key = lambda x: (-1 if sum([dr, dc]) == 1 else 1) * x[abs(dc)]
            movable.sort(key=key)
            for r, c in movable:
                swap((r + dr, c + dc), (r, c))
            position = r + dr, c + dc

    return get_score(grid)

# input_file = 'inputs/test.txt'
input_file = 'inputs/15.txt'
print('#2:', solve(input_file))
