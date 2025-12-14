from itertools import combinations
from my_utils import get_data


# https://adventofcode.com/2025/day/9


def solve_1(data: list[str]) -> int:
    tiles = (tuple(map(int, line.split(','))) for line in data)
    max_distance = 0
    for (x1, y1), (x2, y2) in combinations(tiles, 2):
        dist = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        max_distance = max(max_distance, dist)

    return max_distance


if __name__ == '__main__':
    example = get_data('inputs/09_example.in')
    data_input = get_data('inputs/09.in')
    print(f'Example #1: {solve_1(example)}')
    print(f'Score   #1: {solve_1(data_input)}')
    # print(f'Example #2: {solve_2(example)}')
    # print(f'Score   #2: {solve_2(data_input)}')
