import re
from my_utils import get_data


# https://adventofcode.com/2022/day/15

def parse_data(input_file: str) -> list:
    coordinates = []
    for line in get_data(input_file):
        sx, sy, bx, by = map(int, re.findall(r'\-?\d+', line))
        coordinates.append((sx, sy, bx, by))

    return coordinates


def cannot_contains(coordinates: list, y: int) -> None:
    cannot_contains = set()
    known = set()

    for line in coordinates:
        sx, sy, bx, by = line
        max_distance = abs(sx - bx) + abs(sy - by)
        offset = max_distance - abs(sy - y)

        if offset < 0:
            continue

        lx = sx - offset
        hx = sx + offset

        # TODO optimize
        # part 1 - OK
        # part 2 - impossible.
        # try to go through only uniq intervals...
        for x in range(lx, hx + 1):
            cannot_contains.add(x)

        if by == y:
            known.add(bx)

    print(len(cannot_contains - known))


if __name__ == '__main__':
    # example = parse_data('inputs/15_example.in')
    # cannot_contains(example, y=10)
    data = parse_data('inputs/15.in')
    cannot_contains(data, y=2_000_000)
