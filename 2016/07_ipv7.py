import re
from itertools import chain
from my_utils import get_data


# https://adventofcode.com/2016/day/7


re_inside = re.compile(r'\[(.*?)\]')
re_all = re.compile(r'[^[\]]+')


def check_valid_palindrom(s: str) -> bool:
    for item in zip(s, s[1:], s[2:], s[3:]):
        a, b = item[:2], item[2:]

        if a == b[::-1] and a != b:
            return True

    return False


def get_aba_sequences(s: str) -> set[str]:
    sequences = set()
    for item in zip(s, s[1:], s[2:]):
        a, b, c = item[0], item[1], item[2]

        if a == c and a != b:
            sequences.add(f'{a}{b}{c}')

    return sequences


def solve_1(data: list[str]) -> int:
    valid_ips = set()

    for line in data:
        all_items = re_all.findall(line)
        inside_items = re_inside.findall(line)
        outside_items = [x for x in all_items if x not in inside_items]

        is_inside = False
        is_outside = False

        for i in inside_items:
            if check_valid_palindrom(i):
                is_inside = True
                break

        if is_inside:
            continue

        for o in outside_items:
            if check_valid_palindrom(o):
                is_outside = True
                break

        if is_outside:
            valid_ips.add(line)

    return len(valid_ips)


def solve_2(data: list[str]) -> int:
    valid_ips = set()

    for line in data:
        all_items = re_all.findall(line)
        inside_items = re_inside.findall(line)
        outside_items = [x for x in all_items if x not in inside_items]

        inside_valid = list(chain.from_iterable(
            [get_aba_sequences(i) for i in inside_items]))
        outside_valid = list(chain.from_iterable(
            [get_aba_sequences(o) for o in outside_items]))

        for i in inside_valid:
            ia, ib, _ = i

            for o in outside_valid:
                oa, ob, _ = o

                if ia == ob and ib == oa:
                    valid_ips.add(line)
                    break

    return len(valid_ips)


if __name__ == '__main__':
    input_data = get_data('inputs/07.in')
    print(f'Part 1: {solve_1(input_data)}')
    print(f'Part 2: {solve_2(input_data)}')
