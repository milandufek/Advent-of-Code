from functools import reduce
from itertools import combinations
from operator import mul


with open('inputs/24.in') as f:
    numbers = list(map(int, f.read().strip().split('\n')))


def calc_quantum(weight: int):
    min_qe = 99999999999
    weight_group = sum(numbers) // weight

    for r in range(4, 7):  # enough for both (my) parts
        for product in combinations(numbers, r=r):

            if sum(product) != weight_group:
                continue

            qe = reduce(mul, product)

            if qe < min_qe:
                min_qe = qe
                break

    print(f'Min qe ({weight}):', min_qe)


if __name__ == '__main__':
    calc_quantum(3)
    calc_quantum(4)
