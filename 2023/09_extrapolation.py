from my_utils import get_data


# https://adventofcode.com/2023/day/9


def extrapolate(line: list, part: int) -> int:
    if all(val == 0 for val in line):
        return 0

    deltas = [line[i + 1] - line[i] for i in range(len(line) - 1)]
    diff = extrapolate(deltas, part)

    if part == 1:
        return line[-1] + diff

    if part == 2:
        return line[0] - diff

    return 0


def solve(data: list, part: int) -> int:
    score = 0
    for line in data:
        line = list(map(int, line.split()))
        score += extrapolate(line, part)

    return score


if __name__ == '__main__':
    example = get_data('inputs/09_example.in')
    data = get_data('inputs/09.in')
    print(f'Example #1: {solve(example, 1)}')
    print(f'Score #1: {solve(data, 1)}')
    print(f'Example #2: {solve(example, 2)}')
    print(f'Score #2: {solve(data, 2)}')
