from functools import cache
from my_utils import get_data


# https://adventofcode.com/2025/day/7


def solve_1(data: list[str]) -> int:
    start = data[0].index('S')
    beams = {start}
    splits = 0
    for line in data[1:]:
        next_beam = set()
        for b in beams:
            if line[b] == '^':
                splits += 1
                next_beam.update({b - 1, b + 1} & set(range(len(data[0]))))
            else:
                next_beam.add(b)
        beams = next_beam

    return splits


def solve_2(data: list[str]) -> int:

    @cache
    def beam(r: int, c: int) -> int:
        if r >= len(data):
            return 1
        if data[r][c] == '.' or data[r][c] == 'S':
            return beam(r + 1, c)
        elif data[r][c] == '^':
            return beam(r, c - 1) + beam(r, c + 1)
        return 0

    start = (0, data[0].index('S'))

    return beam(*start)


if __name__ == '__main__':
    example = get_data('inputs/07_example.in')
    data_input = get_data('inputs/07.in')
    print(f'Example #1: {solve_1(example)}')
    print(f'Score   #1: {solve_1(data_input)}')
    print(f'Example #2: {solve_2(example)}')
    print(f'Score   #2: {solve_2(data_input)}')
