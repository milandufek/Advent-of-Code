from itertools import pairwise


# https://adventofcode.com/2017/day/1


def parse_input(input_file: str) -> str:
    with open(input_file) as f:
        return f.read().strip()


def solve_1(data: str) -> int:
    return sum(int(a) for a, b in pairwise(data + data[0]) if a == b)


def solve_2(data: str) -> int:
    half = len(data) // 2
    first = slice(half, None)
    second = slice(None, half)

    return sum(2 * int(a) for a, b in zip(data[first], data[second]) if a == b)


if __name__ == '__main__':
    data_input = parse_input('inputs/01.in')
    print(f'Part 1: {solve_1(data_input)}')
    print(f'Part 2: {solve_2(data_input)}')
