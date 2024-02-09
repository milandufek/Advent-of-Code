from pprint import pprint


# https://adventofcode.com/2023/day/13


PRINT_MIRRORS = True


def find_reflection_line(grid: list) -> int:
    for row in range(1, len(grid)):
        above = grid[:row]
        above_flipped = above[::-1]

        below = grid[row:]

        # Cut the overlapping part.
        above_flipped = above_flipped[:len(below)]
        below = below[:len(above)]

        if above_flipped == below:
            if PRINT_MIRRORS:
                pprint(above_flipped[::-1], width=1)
                print('-' * (len(below[0]) + 4))
                pprint(below, width=1)
                print()

            return row

    return 0


def solve_1(input_file: str) -> int:
    with open(input_file) as f:
        blocks = [b.split() for b in f.read().split('\n\n')]

    score = 0
    VERTICAL_MULTIPLIER = 100

    for block in blocks:
        score += find_reflection_line(block) * VERTICAL_MULTIPLIER
        score += find_reflection_line([''.join(x) for x in zip(*block)])

    return score


if __name__ == '__main__':
    print(f"Example #1: {solve_1('inputs/13_example.in')}")
    print(f"Score #1: {solve_1('inputs/13.in')}")
