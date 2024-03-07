# https://adventofcode.com/2017/day/6


def parse_input(file: str) -> list[int]:
    with open(file) as f:
        return list(map(int, f.read().split()))


def solve(banks: list[int]) -> int:
    seen = {}
    cycles = 0
    while tuple(banks) not in seen:
        seen[tuple(banks)] = cycles
        cycles += 1
        max_index = banks.index(max(banks))
        blocks = banks[max_index]
        banks[max_index] = 0
        for i in range(blocks):
            banks[(max_index + 1 + i) % len(banks)] += 1

    print('Part 1:', cycles)
    print('Part 2:', cycles - seen[tuple(banks)])


if __name__ == '__main__':
    data_input = parse_input('inputs/06.in')
    solve(data_input)
