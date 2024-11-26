from collections import Counter
from itertools import combinations
from my_utils import get_data


# https://adventofcode.com/2018/day/2


def solve_1(data: list[str]) -> int:
    two, three = 0, 0
    for line in data:
        counts = Counter(line)

        if 2 in counts.values():
            two += 1

        if 3 in counts.values():
            three += 1

    return two * three


def solve_2(data: list[str]) -> str:
    for a, b in combinations(data, 2):
        diff = [x for x, y in enumerate(a) if b[x] != y]

        if len(diff) == 1:
            index = diff[0]
            return a[:index] + a[index + 1:]

    return ''


if __name__ == '__main__':
    data_input = get_data('inputs/02.in')
    print(f'Part 1: {solve_1(data_input)}')
    print(f'Part 2: {solve_2(data_input)}')
