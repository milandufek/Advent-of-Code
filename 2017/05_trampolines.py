from my_utils import get_data


# https://adventofcode.com/2017/day/5


def solve_1(data: list[int]) -> int:
    index, steps = 0, 0
    while index < len(data):
        steps += 1
        jump = data[index]
        data[index] += 1
        index += jump

    return steps


def solve_2(data: list[int]) -> int:
    index, steps = 0, 0
    while index < len(data):
        steps += 1
        jump = data[index]
        data[index] += -1 if jump >= 3 else 1
        index += jump

    return steps


if __name__ == '__main__':
    data_input = list(map(int, get_data('inputs/05.in')))
    print(f'Part 1: {solve_1(data_input)}')
    data_input = list(map(int, get_data('inputs/05.in')))
    print(f'Part 2: {solve_2(data_input)}')
