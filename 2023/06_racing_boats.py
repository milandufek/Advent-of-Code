from utils import get_data


# https://adventofcode.com/2023/day/6


def race_1(data: list) -> int:
    times, distances = [list(map(int, line.split()[1:])) for line in data]

    score = 1
    for time, dist in zip(times, distances):
        records = 0
        for boost in range(1, time):
            if boost * (time - boost) > dist:
                records += 1

        score *= records

    return score


def race_2(data: list) -> int:
    time, dist = [int(''.join(line.split()[1:])) for line in data]

    score = 0
    for boost in range(1, time):
        if boost * (time - boost) > dist:
            score += 1

    return score


if __name__ == '__main__':
    example = get_data('inputs/06_example.in')
    data = get_data('inputs/06.in')
    print(f'Example #1: {race_1(example)}')
    print(f'Score #1: {race_1(data)}')
    print(f'Example #2: {race_2(example)}')
    print(f'Score #2: {race_2(data)}')
