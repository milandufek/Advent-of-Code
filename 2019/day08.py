from collections import Counter
from itertools import batched


# https://adventofcode.com/2019/day/8


def get_data(path: str) -> str:
    with open(path) as f:
        return f.read().strip()


def solve_1(code: str, x: int, y: int) -> int:
    n = x * y
    min_zeros = (float('inf'), -1)
    for batch in batched(code, n):
        counter = Counter(batch)
        min_zeros = min(min_zeros, (counter['0'], counter['1'] * counter['2']))

    return min_zeros[1]


def solve_2(code: str, x: int, y: int) -> str:
    n = x * y
    image = ['2'] * n
    for i in range(0, len(code), n):
        for j in range(n):
            if image[j] == '2':
                image[j] = code[i + j]

    image = ''.join(image)
    for r in range(y):
        print(image[r * x : r * x + x].replace('0', '⬛').replace('1', '🟩'))


if __name__ == '__main__':
    data_input = get_data('inputs/08.txt')
    print(f'#1: {solve_1(data_input, 25, 6)}')
    print('#2:')
    solve_2(data_input, 25, 6)
