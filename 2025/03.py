from my_utils import get_data


# https://adventofcode.com/2025/day/3


def get_highest_joltage(bank, count) -> str:
    if count == 0:
        return ''

    if count == len(bank):
        return bank

    search_end = len(bank) - count + 1
    max_battery = max(bank[:search_end])
    max_position = bank.index(max_battery)

    return max_battery + get_highest_joltage(bank[max_position + 1:], count - 1)


def solve(data: list[str], n: int = 2) -> int:
    return sum(int(get_highest_joltage(line, n)) for line in data)


if __name__ == '__main__':
    example = get_data('inputs/03_example.in')
    data_input = get_data('inputs/03.in')
    print(f'Example #1: {solve(example)}')
    print(f'Score   #1: {solve(data_input)}')
    print(f'Example #2: {solve(example, 12)}')
    print(f'Score   #2: {solve(data_input, 12)}')
