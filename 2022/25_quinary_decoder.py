from my_utils import get_data


# https://adventofcode.com/2022/day/25


def snafu_to_decimal(snafu_num: str) -> int:
    base = 5
    decimal = 0

    for exp, i in enumerate(reversed(snafu_num)):
        num = 0
        if i == '-':
            num = -1
        elif i == '=':
            num = -2
        else:
            num = int(i)

        decimal += num * (base ** exp)

    return decimal


def decimal_to_snafu(decimal: int) -> str:
    base = 5
    snafu = []
    num = decimal

    while num > 0:
        remainder = num % base
        num //= base

        if remainder == 3:
            snafu_num = '='
            remainder -= 2
            num += 1
        elif remainder == 4:
            snafu_num = '-'
            remainder -= 1
            num += 1
        else:
            snafu_num = str(remainder)

        snafu.append(snafu_num)

    # print(f"{decimal} -> {''.join(reversed(snafu))}")
    return ''.join(reversed(snafu))


def convert(file: str) -> None:
    results = []
    for line in get_data(file):
        results.append(snafu_to_decimal(line))

    total_in_decimal = sum(results)
    total_in_snafu = decimal_to_snafu(total_in_decimal)

    print(f'Total ({file}): {total_in_snafu} (decimal: {total_in_decimal})')


if __name__ == '__main__':
    convert('inputs/25_example.in')
    convert('inputs/25.in')
