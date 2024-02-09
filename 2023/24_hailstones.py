from my_utils import get_data


# https://adventofcode.com/2023/day/24


class HeilStone():

    def __init__(self, px: int, py: int, pz: int, vx: int, vy: int, vz: int):
        self.px = px
        self.py = py
        self.pz = pz
        self.vx = vx
        self.vy = vy
        self.vz = vz

        self.a = vy
        self.b = -vx
        self.c = vy * px - vx * py

    def __str__(self):
        return f'HeilStone({self.px}, {self.py}, {self.pz}, {self.vx}, {self.vy}, {self.vz})'


def solve(_input: str) -> int:
    total = 0

    min = 200_000_000_000_000
    max = 400_000_000_000_000

    data = get_data(_input)

    hailstones = [HeilStone(*map(int, line.replace('@', ',').split(','))) for line in data]

    for i, first in enumerate(hailstones):
        for next in hailstones[:i]:
            a1, b1, c1 = first.a, first.b, first.c
            a2, b2, c2 = next.a, next.b, next.c

            if a1 * b2 == b1 * a2:
                continue

            x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
            y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
            # print('Cross:', x, y)

            # if 7 <= x <= 27 and 7 <= y <= 27:  # example range
            if min <= x <= max and min <= y <= max:
                if all((x - hs.px) * hs.vx >= 0 and (y - hs.py) * hs.vy >= 0 for hs in (first, next)):
                    total += 1

    return total


if __name__ == '__main__':
    example = 'inputs/24_example.in'
    data_file = 'inputs/24.in'
    # print(f'Example #1: {solve(example)}')
    print(f'Score #1: {solve(data_file)}')
