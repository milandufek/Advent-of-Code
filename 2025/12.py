# https://adventofcode.com/2025/day/12


def solve(file: str) -> int:
    with open(file) as f:
        parts = [line.strip().split() for line in f if 'x' in line]

    score = 0
    for part in parts:
        size = list(map(int, part[0].strip(':').split('x')))
        area = size[0] * size[1]
        presents = sum(map(int, part[1:]))

        if area >= presents * 9:
            score += 1

    return score


if __name__ == '__main__':
    example = 'inputs/12_example.in'
    data_input = 'inputs/12.in'
    print(f'Example: {solve(example)}')
    print(f'Score  : {solve(data_input)}')
