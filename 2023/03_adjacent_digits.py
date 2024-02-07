from my_utils import get_data


# https://adventofcode.com/2023/day/3


def check_number(y: int, x: int, data: list) -> bool:
    if y < 0 or y >= len(data) or x < 0 or x >= len(data[y]) or not data[y][x].isnumeric():
        return False

    return True


def solve_1(data: list) -> int:
    first_digits = set()

    for y, line in enumerate(data):
        for x, ch in enumerate(line):

            if ch == '.' or ch.isnumeric():
                continue

            # check adjacent cells for numbers
            for cy in (y - 1, y, y + 1):
                for cx in (x - 1, x, x + 1):
                    if not check_number(cy, cx, data):
                        continue

                    while cx > 0 and data[cy][cx - 1].isnumeric():
                        cx -= 1

                    first_digits.add((cy, cx))

    # count whole numbers from first digits
    score = 0
    num = []
    for y, x in first_digits:
        while x < len(data[y]) and data[y][x].isnumeric():
            num.append(data[y][x])
            x += 1

        score += int(''.join(num))
        num.clear()

    return score


def solve_2(data: list) -> int:
    score = 0

    for y, line in enumerate(data):
        for x, ch in enumerate(line):

            if ch != '*':
                continue

            first_digits = set()

            # check adjacent cells for numbers
            for cy in (y - 1, y, y + 1):
                for cx in (x - 1, x, x + 1):
                    if not check_number(cy, cx, data):
                        continue

                    while cx > 0 and data[cy][cx - 1].isnumeric():
                        cx -= 1

                    first_digits.add((cy, cx))

            if len(first_digits) != 2:
                continue

            # count whole numbers from first digits
            num, nums = [], []
            for dy, dx in first_digits:
                while dx < len(data[dy]) and data[dy][dx].isnumeric():
                    num.append(data[dy][dx])
                    dx += 1

                nums.append(int(''.join(num)))
                num.clear()

            score += nums[0] * nums[1]

    return score


if __name__ == '__main__':
    example = get_data('inputs/03_example.in')
    data = get_data('inputs/03.in')
    print(f'Example #1: {solve_1(example)}')
    print(f'Score #1: {solve_1(data)}')
    print(f'Example #2: {solve_2(example)}')
    print(f'Score #2: {solve_2(data)}')
