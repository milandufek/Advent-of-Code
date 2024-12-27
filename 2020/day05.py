# https://adventofcode.com/2020/day/5


def get_data(file_path: str) -> list[str]:
    with open(file_path) as f:
        return f.readlines()


def get_sids(data: list[str]) -> list[int]:
    sids = []
    for line in data:
        row = line[:7].replace('F', '0').replace('B', '1')
        col = line[7:].replace('L', '0').replace('R', '1')
        sids.append(int(row, 2) * 8 + int(col, 2))

    return sids


def solve_1(data: list[str]) -> int:
    return max(get_sids(data))


def solve_2(data: list[str]) -> int:
    sids = get_sids(data)
    for i in range(min(sids), max(sids)):
        if i not in sids:
            return i


if __name__ == '__main__':
    # data_input = ['FBFBBFFRLR']
    data_input = get_data('inputs/05.txt')
    print(f'#1: {solve_1(data_input)}')
    print(f'#2: {solve_2(data_input)}')
