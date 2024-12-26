# https://adventofcode.com/2019/day/4


def solve_1(num_range: str) -> int:
    start, end = map(int, num_range.split('-'))
    count = 0
    for num in range(start, end + 1):
        num = str(num)
        if sorted(num) == list(num) and any(num.count(d) >= 2 for d in num):
            count += 1

    return count


def solve_2(num_range: str) -> int:
    start, end = map(int, num_range.split('-'))
    count = 0
    for num in range(start, end + 1):
        num = str(num)
        if sorted(num) == list(num) and any(num.count(d) == 2 for d in num):
            count += 1

    return count


if __name__ == '__main__':
    data_input = '125730-579381'
    print('#1:', solve_1(data_input))
    print('#2:', solve_2(data_input))
