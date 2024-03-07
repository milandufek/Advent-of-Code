from my_utils import get_data


# https://adventofcode.com/2017/day/4


def solve_1(data: str) -> int:
    total = 0
    for line in data:
        words = line.strip().split()

        if len(words) == len(set(words)):
            total += 1

    return total


def solve_2(data: str) -> int:
    total = 0
    for line in data:
        words = line.strip().split()
        words = [''.join(sorted(word)) for word in words]

        if len(words) == len(set(words)):
            total += 1

    return total


if __name__ == '__main__':
    data_input = get_data('inputs/04.in')
    print(f'Part 1: {solve_1(data_input)}')
    print(f'Part 2: {solve_2(data_input)}')
