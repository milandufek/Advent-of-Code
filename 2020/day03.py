from functools import reduce


# https://adventofcode.com/2020/day/3


def get_data(file_path: str) -> list[str]:
    with open(file_path) as f:
        return f.readlines()


def solve_1(data: list[str], r_inc: int = 3, c_inc: int = 1) -> int:
    r, c = 0, 0
    trees = 0
    while c < len(data):
        if data[c][r % (len(data[0]) - 1)] == '#':
            trees += 1
        r += r_inc
        c += c_inc

    return trees


def solve_2(data: list[str]) -> int:
    increments = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    mul = lambda x, y: x * y
    return reduce(mul, (solve_1(data, r, c) for r, c in increments))


if __name__ == '__main__':
    # data_input = get_data('inputs/test.txt')
    data_input = get_data('inputs/03.txt')
    print(f'#1: {solve_1(data_input)}')
    print(f'#2: {solve_2(data_input)}')
