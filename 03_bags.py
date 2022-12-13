from utils import get_data


# https://adventofcode.com/2022/day/3

CHARS = ['_'] + \
    [chr(low) for low in range(ord('a'), ord('z') + 1)] + \
    [chr(upp) for upp in range(ord('A'), ord('Z') + 1)]


def get_priorities(data: list) -> int:
    priority_count = 0
    for item in data:
        half_length = int(len(item) / 2)
        first_part = set(item[:half_length])
        second_part = set(item[half_length:])
        for ch in first_part:
            if ch in second_part:
                priority_count += CHARS.index(ch)

    return priority_count


def get_group_priorities(data: list) -> int:
    priority_count = 0
    group = []
    for item in data:
        group.append(item)
        if len(group) == 3:
            first = set(group[0])
            second = set(group[1])
            third = set(group[2])
            for ch in first:
                if ch in second and ch in third:
                    priority_count += CHARS.index(ch)
            group.clear()

    return priority_count


if __name__ == '__main__':
    small_data = [
        'vJrwpWtwJgWrhcsFMMfFFhFp',
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
        'PmmdzqPrVvPwwTWBwg',
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
        'ttgJtRGJQctTZtZT',
        'CrZsJsPPZsGzwwsLwLmpwMDw',
    ]
    data = get_data('inputs/03.in')

    print('Example 1:', get_priorities(small_data))
    print('Batch 1:', get_priorities(data))
    print('Example 2:', get_group_priorities(small_data))
    print('Batch 2:', get_group_priorities(data))
