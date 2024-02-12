from my_utils import get_data


# https://adventofcode.com/2023/day/14


def cycle(grid: tuple) -> tuple:
    flipped = tuple(map(''.join, zip(*grid)))
    tilted = ('#'.join([''.join(sorted(tuple(group), reverse=True))
              for group in row.split('#')])
              for row in flipped)
    flipped_back = tuple(r[::-1] for r in tilted)

    return flipped_back


def four_cycles(grid: tuple) -> tuple:
    for _ in range(4):
        grid = cycle(grid)

    return grid


def count_score(grid: tuple) -> int:
    return sum(row.count('O') * (len(grid) - r)
               for r, row in enumerate(grid))


def solve_1(grid: tuple) -> int:
    return count_score(cycle(grid))


def solve_2(grid: tuple) -> int:
    states = [grid]
    seen = {grid}
    cycles = 1_000_000_000

    for i in range(cycles):
        grid = four_cycles(grid)

        if grid in seen:
            break

        seen.add(grid)
        states.append(grid)

    first_seen = states.index(grid)
    grid = states[(cycles - first_seen) % (i - first_seen) + first_seen]

    return count_score(grid)


if __name__ == '__main__':
    example = tuple(get_data('inputs/14_example.in'))
    data_input = tuple(get_data('inputs/14.in'))
    print(f'Example #1: {solve_1(example)}')
    print(f'Score #1: {solve_1(data_input)}')
    print(f'Example #2: {solve_2(example)}')
    print(f'Score #2: {solve_2(data_input)}')
