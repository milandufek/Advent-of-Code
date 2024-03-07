import math


# https://adventofcode.com/2017/day/3


def solve_1(n: int) -> int:
    side_length = math.ceil(math.sqrt(n))
    side_center = side_length // 2
    distance_from_corner = n - (side_length - 2) ** 2
    distance_from_center = abs(distance_from_corner % (side_length - 1) - side_center)
    manhattan_distance = side_center + distance_from_center

    return manhattan_distance


def get_next(x: int, y: int) -> tuple[int, int]:
    if -x < y < x:
        return x, y + 1

    if y > -x and y >= x:
        return x - 1, y

    if x < y <= -x:
        return x, y - 1

    if x >= y <= -x:
        return x + 1, y

    if x == y == 0:
        return 1, 0

    return None


def solve_2(n: int) -> int:
    x, y = 0, 0
    spiral = {(0, 0): 1}

    while spiral[(x, y)] <= n:
        x, y = get_next(x, y)
        spiral[(x, y)] = sum(
            spiral.get((x + r, y + c), 0)
            for r in (-1, 0, 1) for c in (-1, 0, 1)
        )

    return spiral[(x, y)]


if __name__ == '__main__':
    my_num = 265149
    print(f'Part 1: {solve_1(my_num)}')
    print(f'Part 2: {solve_2(my_num)}')
