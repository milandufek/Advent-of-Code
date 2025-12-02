from itertools import batched


# https://adventofcode.com/2025/day/2


def get_data(file_path) -> str:
    with open(file_path) as f:
        return f.read().strip()


def is_valid(seq: str) -> bool:
    a = seq[:len(seq) // 2]
    b = seq[len(seq) // 2:]
    return a != b


def is_valid_v2(seq: str) -> bool:
    i = int(len(seq) / 2)
    for n in range(1, i + 1):
        batch = list(batched(seq, n))
        if len(set(batch)) == 1:
            return False
    return True


def solve(s: str) -> tuple[int, int]:
    ranges = s.split(',')
    invalid_1, invalid_2 = [], []
    for range_nums in ranges:
        start, end = map(int, range_nums.split('-'))
        for num in range(start, end + 1):
            if not is_valid(str(num)):
                invalid_1.append(num)
            if not is_valid_v2(str(num)):
                invalid_2.append(num)

    return sum(invalid_1), sum(invalid_2)


if __name__ == '__main__':
    # example = get_data('inputs/02_example.in')
    data_input = get_data('inputs/02.in')
    # example_2 = get_data('inputs/02_example_2.in')
    part1, part2 = solve(data_input)
    print(f'Score #1: {part1}')
    print(f'Score #2: {part2}')
