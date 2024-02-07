from collections import defaultdict
from my_utils import get_data


# https://adventofcode.com/2023/day/4


def solve_1(data: list) -> int:
    score = 0

    for line in data:
        _, cards = line.split(':')
        left, right = [set(map(int, x.split())) for x in cards.strip().split(' | ')]
        matches = len(left & right)

        if matches > 0:
            score += 2 ** (matches - 1)

    return score


def solve_2(data: list) -> int:
    counter = defaultdict(int)

    for i, line in enumerate(data):
        counter[i] += 1
        _, cards = line.split(':')
        left, right = [set(map(int, x.split())) for x in cards.strip().split(' | ')]
        matches = len(left & right)

        for j in range(matches):
            counter[i + j + 1] += counter[i]

    return sum(counter.values())


if __name__ == '__main__':
    example = get_data('inputs/04_example.in')
    data = get_data('inputs/04.in')
    print(f'Example #1: {solve_1(example)}')
    print(f'Score #1: {solve_1(data)}')
    print(f'Example #2: {solve_2(example)}')
    print(f'Score #2: {solve_2(data)}')
