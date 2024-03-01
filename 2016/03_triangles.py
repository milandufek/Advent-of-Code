from itertools import batched


# https://adventofcode.com/2016/day/3


def parse_input(file: str) -> list[tuple[int, int, int]]:
    with open(file) as f:
        return [tuple(map(int, line.split())) for line in f.read().splitlines()]


def is_triangle(a: int, b: int, c: int) -> bool:
    return a + b > c and a + c > b and b + c > a


def solve_1(sides: list[tuple[int, int, int]]):
    return sum(1 for a, b, c in sides if is_triangle(a, b, c))


def solve_2(numbers: list[tuple[int, int, int]]) -> int:
    sides = []
    for batch in batched(numbers, 3):
        for i in range(3):
            first, second, third = batch
            sides.append((first[i], second[i], third[i]))

    return sum(1 for a, b, c in sides if is_triangle(a, b, c))


if __name__ == '__main__':
    data_input = parse_input('inputs/03.in')
    print(f'Part 1: {solve_1(data_input)}')
    print(f'Part 2: {solve_2(data_input)}')
