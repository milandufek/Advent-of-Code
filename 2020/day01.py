from functools import reduce
from itertools import combinations
from operator import mul


# https://adventofcode.com/2020/day/1


numbers = [
    1721,
    979,
    366,
    299,
    675,
    1456,
]

SUM = 2020

with open('inputs/01.txt') as f:
    numbers = list(map(int, f.readlines()))

score_1 = reduce(mul, *[x for x in combinations(numbers, 2) if sum(x) == SUM])
print(f'#1: {score_1}')

score_2 = reduce(mul, *[x for x in combinations(numbers, 3) if sum(x) == SUM])
print(f'#2: {score_2}')
