import re
from collections import Counter
from dataclasses import dataclass


# https://adventofcode.com/2018/day/3


@dataclass
class Claim:
    id: int
    x: int
    y: int
    width: int
    height: int


def parse_input(file_name: str) -> list[Claim]:
    re_numbers = re.compile(r'\d+')
    with open(file_name) as f:
        return [
            Claim(*map(int, re_numbers.findall(line)))
            for line in f.read().splitlines()
        ]


def solve(claims: list[Claim]) -> int:
    grid = Counter()
    for claim in claims:
        for x in range(claim.x, claim.x + claim.width):
            for y in range(claim.y, claim.y + claim.height):
                grid[x, y] += 1

    print(f'Part 1: {sum(1 for count in grid.values() if count > 1)}')

    for claim in claims:
        if all(
            grid[x, y] == 1
            for x in range(claim.x, claim.x + claim.width)
            for y in range(claim.y, claim.y + claim.height)
        ):
            print(f'Part 2: {claim.id}')


if __name__ == '__main__':
    data_input = parse_input('inputs/03.in')
    solve(data_input)
