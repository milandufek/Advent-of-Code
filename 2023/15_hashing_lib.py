# https://adventofcode.com/2023/day/15


def get_hash(s: str) -> int:
    val = 0

    for ch in s:
        val += ord(ch)
        val *= 17
        val %= 256

    return val


def solve_1(_input: str) -> int:
    with open(_input) as f:
        data = f.read().strip().split(',')

    return sum(map(get_hash, data))


if __name__ == '__main__':
    example = 'inputs/15_example.in'
    data_file = 'inputs/15.in'
    print(f'Example #1: {solve_1(example)}')
    print(f'Score #1: {solve_1(data_file)}')
