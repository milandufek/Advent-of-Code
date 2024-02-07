from collections import defaultdict
from functools import reduce
from my_utils import get_data


# https://adventofcode.com/2023/day/2


MAX_VALUES = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def solve_1(_input: list) -> int:
    score = 0

    for line in _input:
        invalid = False
        game_num, moves = line.split(':')
        game_num = int(game_num.split(' ')[1])

        for m in moves.split(';'):
            for pack in m.split(','):
                count, color = pack.strip().split(' ')
                count = int(count)

                if count > MAX_VALUES[color]:
                    invalid = True
                    break

        if invalid:
            continue

        score += game_num

    return score


def solve_2(_input: list) -> int:
    score = 0

    for line in _input:
        max_count = defaultdict(int)
        game_num, moves = line.split(':')
        game_num = int(game_num.split(' ')[1])

        for m in moves.split(';'):
            for cube in m.split(','):
                count, color = cube.strip().split(' ')
                max_count[color] = max(int(count), max_count[color])

        score += reduce(lambda x, y: x * y, max_count.values())

    return score


if __name__ == '__main__':
    example = get_data('inputs/02_example.in')
    data = get_data('inputs/02.in')
    print(f'Example #1: {solve_1(example)}')
    print(f'Score #1: {solve_1(data)}')
    print(f'Example #2: {solve_2(example)}')
    print(f'Score #2: {solve_2(data)}')
