from my_utils import get_data


# https://adventofcode.com/2022/day/1

def max_count(list_: list) -> int:
    count = 0
    max_count = 0
    for i in list_:
        if i:
            count += int(i)
        else:
            if count > max_count:
                max_count = count
            count = 0

    return max_count


def top_three_count(list_: list) -> int:
    count = 0
    sum_calories = []
    for i in list_:
        if i:
            count += int(i)
        else:
            sum_calories.append(count)
            count = 0

    return sum(sorted(sum_calories, reverse=True)[:3])


if __name__ == '__main__':
    data = get_data('inputs/01.in')
    print('Top count:', max_count(data))
    print('Top three count:', top_three_count(data))
