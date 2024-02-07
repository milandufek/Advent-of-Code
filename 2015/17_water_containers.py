from collections import Counter
from itertools import combinations
from utils import get_data


LITERS = 150
containers = sorted(list(map(int, get_data('inputs/17.in'))))

all_possible = []
# 4-9, less or more is not possible (in my case) -> len(containers) universal
for r in range(4, 9):
    for comb in combinations(containers, r=r):
        if sum(comb) == LITERS:
            all_possible.append(comb)

print(f'Total #1 (all): {len(all_possible)}')

counter = Counter(len(x) for x in all_possible)
minimal = min(counter.items(), key=lambda x: x[0])[1]

print(f'Total #2 (minimal): {minimal}')
