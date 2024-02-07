from itertools import cycle
from utils import get_data


# https://adventofcode.com/2023/day/8


def solve(_input: str) -> int:
    data = get_data(_input)
    moves = data[0]
    nodes = data[2:]

    network = {}

    for line in nodes:
        pos, targets = line.split(' = ')
        targets = targets[1:-1].split(', ')
        network[pos] = targets

    count = 0
    current = 'AAA'
    end = 'ZZZ'

    for m in cycle(moves):
        count += 1
        current = network[current][0 if m == 'L' else 1]

        if current == end:
            return count


if __name__ == '__main__':
    example = 'inputs/08_example.in'
    data = 'inputs/08.in'
    print(f'Example #1: {solve(example)}')
    print(f'Score #1: {solve(data)}')
