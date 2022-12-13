from utils import get_data


# https://adventofcode.com/2022/day/4

def cleanup(data: list) -> int:
    count_subsets = 0
    count_intersection = 0

    for pair in data:
        first, second = tuple(pair.split(','))
        first_range = first.split('-')
        second_range = second.split('-')
        first_set = set(range(int(first_range[0]), int(first_range[1]) + 1))
        second_set = set(range(int(second_range[0]), int(second_range[1]) + 1))

        # part 1
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            count_subsets += 1

        # part 2
        if first_set.intersection(second_set):
            count_intersection += 1

    return count_subsets, count_intersection


if __name__ == '__main__':
    example = [
        '2-4,6-8',
        '2-3,4-5',
        '5-7,7-9',
        '2-8,3-7',
        '6-6,4-6',
        '2-6,4-8',
    ]
    data = get_data('inputs/04.in')
    print('Example:', cleanup(example))
    print('Batch:', cleanup(data))
