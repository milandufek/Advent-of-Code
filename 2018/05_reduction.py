import string
from my_utils import get_data


# https://adventofcode.com/2018/day/5


def solve_1(s: str) -> int:
    stack = []
    for ch in s:
        if stack and stack[-1] != ch and stack[-1].lower() == ch.lower():
            stack.pop()
        else:
            stack.append(ch)

    return len(stack)


def solve_2(s: str) -> int:
    return min(
        solve_1(s.replace(ch, '').replace(ch.upper(), ''))
        for ch in string.ascii_lowercase
    )


if __name__ == '__main__':
    example_input = 'dabAcCaCBAcCcaDA'
    data_input = get_data('inputs/05.in')[0]
    print(f'Part 1: {solve_1(data_input)}')
    print(f'Part 2: {solve_2(data_input)}')
