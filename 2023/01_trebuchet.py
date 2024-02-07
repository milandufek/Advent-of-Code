from my_utils import get_data


# https://adventofcode.com/2023/day/1


NUMBERS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def find_first(line: str) -> int:
    s = ''

    for i in line:
        if i.isdigit():
            return int(i)

        s += i

        for n in NUMBERS:
            if n in s:
                return NUMBERS.index(n)


def find_last(line: str) -> int:
    s = ''

    for i in reversed(line):
        if i.isdigit():
            return int(i)

        s = i + s

        for n in NUMBERS:
            if n in s:
                return NUMBERS.index(n)


def solve(data: list) -> int:
    return sum(list(int(f'{find_first(line)}{find_last(line)}') for line in data))


if __name__ == '__main__':
    # example = get_data('inputs/01_example.in')
    example = get_data('inputs/01_example_2.in')
    # example = get_data('inputs/01_example_m.in')
    data = get_data('inputs/01.in')

    # print(f'Example #1: {solve(example)}')
    # print(f'#1: {solve(data)}')
    print(f'Example #2: {solve(example)}')
    print(f'Sum #2: {solve(data)}')
