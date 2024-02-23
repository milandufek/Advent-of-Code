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


def intersection(hs1: HeilStone, hs2: HeilStone) -> tuple[int, int]:
    a1, b1, c1 = hs1.a, hs1.b, hs1.c
    a2, b2, c2 = hs2.a, hs2.b, hs2.c

    if a1 * b2 == b1 * a2:
        return 0, 0

    # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
    x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
    y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
    # print(f'Cross:  {x = :>20}  {y = :>20}')

    return x, y


def solve(_input: str, imin: int, imax: int) -> int:
    total = 0
    data = get_data(_input)
    hailstones = [HeilStone(*map(int, line.replace('@', ',').split(',')))
                  for line in data]

    for i, first in enumerate(hailstones):
        for _next in hailstones[:i]:
            x, y = intersection(first, _next)

            if imin <= x <= imax and imin <= y <= imax:
                if all((x - hs.px) * hs.vx >= 0 and (y - hs.py) * hs.vy >= 0
                       for hs in (first, _next)):
                    total += 1

    return total


if __name__ == '__main__':
    example = 'inputs/24_example.in'
    print(f'Example #1: {solve(example, 7, 27)}')

    data_file = 'inputs/24.in'
    imin = 200_000_000_000_000
    imax = 400_000_000_000_000
    print(f'Score #1: {solve(data_file, imin, imax)}')
