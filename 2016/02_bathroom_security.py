from my_utils import get_data


# https://adventofcode.com/2016/day/2


def solve_1(instructions: list) -> int:
    grid = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    position = (1, 1)
    code = []

    for line in instructions:
        for move in line:
            x, y = position

            match move:
                case 'L':
                    position = (max(0, x - 1), y)
                case 'R':
                    position = (min(2, x + 1), y)
                case 'U':
                    position = (x, max(0, y - 1))
                case 'D':
                    position = (x, min(2, y + 1))

        x, y = position
        code.append(grid[y][x])

    return int(''.join(map(str, code)))


def solve_2(instructions: list) -> str:
    grid = (
        ('#', '#', '1', '#', '#'),
        ('#', '2', '3', '4', '#'),
        ('5', '6', '7', '8', '9'),
        ('#', 'A', 'B', 'C', '#'),
        ('#', '#', 'D', '#', '#')
    )
    position = (0, 2)
    code = []

    def get_min_max(n: int) -> int:
        n = max(0, n)
        n = min(n, len(grid) - 1)
        return n

    for line in instructions:
        for move in line:
            x, y = position
            cx, cy = position

            match move:
                case 'L':
                    position = (get_min_max(x - 1), y)
                case 'R':
                    position = (get_min_max(x + 1), y)
                case 'U':
                    position = (x, get_min_max(y - 1))
                case 'D':
                    position = (x, get_min_max(y + 1))

            x, y = position
            if grid[y][x] == '#':
                position = (cx, cy)

        code.append(grid[y][x])

    return ''.join(code)


if __name__ == '__main__':
    example = get_data('inputs/02_example.in')
    data_input = get_data('inputs/02.in')
    print(f'Example 1: {solve_1(example)}')
    print(f'Part 1: {solve_1(data_input)}')
    print(f'Example 2: {solve_2(example)}')
    print(f'Part 2: {solve_2(data_input)}')
