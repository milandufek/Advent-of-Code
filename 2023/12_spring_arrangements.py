import functools
from my_utils import get_data


# https://adventofcode.com/2023/day/12


@functools.cache
def get_count(s: str, nums: tuple[int]) -> int:
    if not s:
        return 1 if nums == () else 0

    if not nums:
        return 0 if '#' in s else 1

    count = 0

    if s[0] in '.?':
        count += get_count(s[1:], nums)

    if s[0] in '#?':
        if (
            nums[0] <= len(s)
            and '.' not in s[:nums[0]]
            and (nums[0] == len(s) or s[nums[0]] != '#')
        ):
            count += get_count(s[nums[0] + 1:], nums[1:])

    return count


def solve(data: list, part: int = 1) -> int:
    score = 0

    for line in data:
        springs, nums = line.split()
        nums = tuple(map(int, nums.split(',')))

        if part == 2:
            MULTIPLIER = 5
            nums *= MULTIPLIER
            springs = '?'.join([springs] * MULTIPLIER)

        score += get_count(springs, nums)

    return score


if __name__ == '__main__':
    example = get_data('inputs/12_example.in')
    data = get_data('inputs/12.in')
    print(f'Example #1: {solve(example)}')
    print(f'Score #1: {solve(data)}')
    print(f'Example #2: {solve(example, 2)}')
    print(f'Score #2: {solve(data, 2)}')
