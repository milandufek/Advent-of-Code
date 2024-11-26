from itertools import cycle


def parse_input(file_name: str) -> list[int]:
    with open(file_name) as f:
        return list(map(int, f.readlines()))


def solve_1(nums: list[int]) -> None:
    return sum(nums)


def solve_2(nums: list[int]) -> None:
    x = 0
    results = {x: 1}

    for i in cycle(nums):
        x += i

        if results.get(x):
            break

        results[x] = 1

    return x


if __name__ == '__main__':
    data_input = parse_input('inputs/01.in')
    print(f'Part 1: {solve_1(data_input)}')
    print(f'Part 2: {solve_2(data_input)}')
