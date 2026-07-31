from itertools import pairwise
from collections import Counter
from my_utils import get_data


# https://adventofcode.com/2021/day/14


def parse_input(data: list[str]) -> tuple[str, dict[str, str]]:
    template = data[0]
    rules = dict(item.split(' -> ') for item in data[2:])
    return template, rules


def polymerize(data: list[str], steps: int) -> int:
    template, rules = parse_input(data)
    pair_counts = Counter(map(''.join, pairwise(template)))
    element_counts = Counter(template)

    for _ in range(steps):
        new_pair_counts = Counter()

        for pair, count in pair_counts.items():
            if pair in rules:
                insert = rules[pair]
                new_pair_counts[pair[0] + insert] += count
                new_pair_counts[insert + pair[1]] += count
                element_counts[insert] += count
            else:
                new_pair_counts[pair] += count

        pair_counts = new_pair_counts

    return max(element_counts.values()) - min(element_counts.values())


def solve_1(data: list[str], steps: int = 10) -> int:
    return polymerize(data, steps)


def solve_2(data: list[str], steps: int = 40) -> int:
    return polymerize(data, steps)


if __name__ == '__main__':
    data_input = get_data('inputs/14.in')
    print(f'#1: {solve_1(data_input)}')
    print(f'#2: {solve_2(data_input)}')
