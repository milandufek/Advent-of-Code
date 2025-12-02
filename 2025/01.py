from my_utils import get_data


# https://adventofcode.com/2025/day/1


def solve_1(moves: list[str]) -> int:
    point = 50
    counter = 0
    for move in moves:
        dir, step = move[0], int(move[1:])

        if dir == 'L':
            point = (point - step) % 100
        elif dir == 'R':
            point = (point + step) % 100

        if point == 0:
            counter += 1

    return counter


def solve_2(moves: list[str]) -> int:
    point = 50
    counter = 0
    current_dir = 'R'
    for move in moves:
        dir, step = move[0], int(move[1:])

        if dir != current_dir:
            point = (100 - point) % 100  # reverse direction
            current_dir = dir

        point += step
        counter += point // 100
        point %= 100

    return counter


if __name__ == '__main__':
    example = get_data('inputs/01_example.in')
    data_input = get_data('inputs/01.in')
    print(f'Example #1: {solve_1(example)}')
    print(f'Score   #1: {solve_1(data_input)}')
    print(f'Example #2: {solve_2(example)}')
    print(f'Score   #2: {solve_2(data_input)}')
