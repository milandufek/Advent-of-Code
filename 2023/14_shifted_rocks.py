from my_utils import get_data


# https://adventofcode.com/2023/day/14


def solve_1(data:list) -> int:
    flipped = list(map(''.join, zip(*data)))
    tilted = ['#'.join([''.join(sorted(list(group), reverse=True))
                        for group in row.split('#')])
                        for row in flipped]
    grid = list(map(''.join, zip(*tilted)))

    return sum(row.count('O') * (len(grid) - r) for r, row in enumerate(grid))


if __name__ == '__main__':
    example = get_data('inputs/14_example.in')
    data = get_data('inputs/14.in')
    print(f'Example #1: {solve_1(example)}')
    print(f'Score #1: {solve_1(data)}')
