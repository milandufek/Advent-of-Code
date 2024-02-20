from collections import deque
from my_utils import get_data


# https://adventofcode.com/2023/day/22


class Brick:

    def __init__(self, line) -> None:
        start, end = line.split('~')
        self.xs, self.ys, self.z_bottom = map(int, start.split(','))
        self.xe, self.ye, self.z_top = map(int, end.split(','))

    def __repr__(self) -> str:
        return f'Brick({self.xs}-{self.xe},{self.ys}-{self.ye},{self.z_bottom}-{self.z_top})'

    def overlaps(self, other) -> bool:
        return (
            self.xs <= other.xe and self.xe >= other.xs and
            self.ys <= other.ye and self.ye >= other.ys
        )


def sort_bricks(bricks: list) -> list[Brick]:
    bricks = [Brick(line) for line in bricks]
    bricks.sort(key=lambda brick: brick.z_bottom)

    # Sort bricks vertically from bottom up.
    for i, brick in enumerate(bricks):
        max_z = 0
        for other in bricks[:i]:
            if brick.overlaps(other):
                max_z = max(max_z, other.z_top + 1)

        brick.z_top -= brick.z_bottom - max_z
        brick.z_bottom = max_z

    bricks.sort(key=lambda brick: brick.z_bottom)

    return bricks


def get_bricks_overlapping(_input: list) -> list[list, set, set]:
    bricks = sort_bricks(_input)
    k_supports_v = {x: set() for x in range(len(bricks))}
    v_supports_k = {x: set() for x in range(len(bricks))}

    for upper_index, upper in enumerate(bricks):
        for lower_index, lower in enumerate(bricks[:upper_index]):
            if lower.overlaps(upper) and lower.z_top + 1 == upper.z_bottom:
                k_supports_v[lower_index].add(upper_index)
                v_supports_k[upper_index].add(lower_index)

    return bricks, k_supports_v, v_supports_k


def solve_1(_input: list) -> int:
    bricks, k_supports_v, v_supports_k = get_bricks_overlapping(_input)
    total = 0

    for i in range(len(bricks)):
        if all(len(v_supports_k[j]) > 1 for j in k_supports_v[i]):
            total += 1

    return total


def solve_2(_input: list) -> int:
    bricks, k_supports_v, v_supports_k = get_bricks_overlapping(_input)
    total = 0

    for i in range(len(bricks)):
        queue = deque(j for j in k_supports_v[i] if len(v_supports_k[j]) == 1)
        falling = set(queue)
        falling.add(i)

        while queue:
            j = queue.popleft()
            for k in k_supports_v[j] - falling:
                if v_supports_k[k] <= falling:
                    queue.append(k)
                    falling.add(k)

        total += len(falling) - 1

    return total


if __name__ == '__main__':
    example = get_data('inputs/22_example.in')
    data_input = get_data('inputs/22.in')
    print(f'Example #1: {solve_1(example)}')
    print(f'Score #1: {solve_1(data_input)}')
    print(f'Example #2: {solve_2(example)}')
    print(f'Score #2: {solve_2(data_input)}')
