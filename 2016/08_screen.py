from my_utils import get_data


# https://adventofcode.com/2016/day/8


PIXEL_ON = '🟩'
PIXEL_OFF = '⬛'


def get_empty_screen(cols, rows) -> list[list[str]]:
    return [[PIXEL_OFF for _ in range(cols)] for _ in range(rows)]


def print_screen(grid) -> None:
    print('\n'.join([''.join(row) for row in grid]))
    print()


def count_lit_pixels(screen: list[list[str]]) -> int:
    return sum(row.count(PIXEL_ON) for row in screen)


def parse_instruction(instruction: str) -> tuple[str, int, int]:
    if instruction.startswith('rect'):
        row, col = map(int, instruction.split(' ')[1].split('x'))
        return 'rect', row, col

    if instruction.startswith('rotate '):
        row_or_col = instruction.split(' ')[1]
        xy = int(instruction.split(' ')[2].split('=')[1])
        by = int(instruction.split(' ')[4])
        return f'rotate {row_or_col}', xy, by

    raise ValueError(f'Invalid instruction: {instruction}')


def fill_rect(screen: list[list[str]], col: int, row: int) -> list[list[str]]:
    for r in range(row):
        for c in range(col):
            screen[r][c] = PIXEL_ON

    return screen


def rotate_row(screen: list[list[str]], row: int, by: int) -> list[list[str]]:
    screen[row] = screen[row][-by:] + screen[row][:-by]
    return screen


def rotate_col(screen: list[list[str]], col: int, by: int) -> list[list[str]]:
    col_values = [screen[r][col] for r in range(len(screen))]
    col_values = col_values[-by:] + col_values[:-by]
    for r, row in enumerate(screen):
        row[col] = col_values[r]

    return screen


def solve(instructions: list[str]) -> None:
    screen = get_empty_screen(50, 6)
    instructions = [parse_instruction(i) for i in instructions]

    for instruction, *args in instructions:
        if instruction == 'rect':
            screen = fill_rect(screen, *args)
        elif instruction == 'rotate row':
            screen = rotate_row(screen, *args)
        elif instruction == 'rotate column':
            screen = rotate_col(screen, *args)

    print('Part 1:', count_lit_pixels(screen))
    print('Part 2:')
    print_screen(screen)


if __name__ == '__main__':
    data_input = get_data('inputs/08.in')
    solve(data_input)
