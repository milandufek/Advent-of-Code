
from functools import reduce
from operator import mul
from itertools import combinations


with open('inputs/01.in') as f:
    lines = list(map(int, f.readlines()))

for i in combinations(lines, r=2):
    if sum(i) == 2020:
        print('#1:', i[0] * i[1])

for i in combinations(lines, r=3):
    if sum(i) == 2020:
        print('#2:', reduce(mul, i))
