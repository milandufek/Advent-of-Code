# https://adventofcode.com/2017/day/2


def parse_input(input_file: str) -> list[list[int]]:
    with open(input_file) as f:
        return [[int(num) for num in line.split()] for line in f]


def solve_1(data: list[list[int]]) -> int:
    return sum(max(row) - min(row) for row in data)


def solve_2(data: list[list[int]]) -> int:
    return sum(
        next(a // b for a in row for b in row if a != b and a % b == 0)
        for row in data
    )


if __name__ == '__main__':
    data_input = parse_input('inputs/02.in')
    print(f'Part 1: {solve_1(data_input)}')
    print(f'Part 2: {solve_2(data_input)}')
