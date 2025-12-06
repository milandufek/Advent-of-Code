from functools import reduce
from itertools import pairwise
from operator import mul
from my_utils import get_data


# https://adventofcode.com/2025/day/6


def solve_1(data: list[str]) -> int:
    cols = list(zip(*(x.split() for x in data)))
    score = 0
    for col in cols:
        vals, op = list(map(int, col[:-1])), col[-1]
        if op == '+':
            score += sum(vals)
        elif op == '*':
            score += reduce(mul, vals)

    return score


def solve_2(data: list[str]) -> int:
    ops = data[-1]
    split_indexes = [i for i, x in enumerate(ops) if x in '+*']
    split_indexes.append(len(ops) + 1)
    ranges = list(pairwise(split_indexes))
    rows = []
    for i in range(len(data)):
        cols = []
        for start, end in ranges:
            cols.append(data[i][start:end - 1])
        rows.append(cols)

    swapped_rows = zip(*rows)
    score = 0
    for row in swapped_rows:
        nums, op = row[:-1], row[-1].strip()
        nums = (int(''.join(v).strip()) for v in zip(*nums))
        score += sum(nums) if op == '+' else reduce(mul, nums)

    return score


if __name__ == '__main__':
    example = get_data('inputs/06_example.in')
    data_input = get_data('inputs/06.in')
    print(f'Example #1: {solve_1(example)}')
    print(f'Score   #1: {solve_1(data_input)}')
    print(f'Example #2: {solve_2(example)}')
    print(f'Score   #2: {solve_2(data_input)}')
