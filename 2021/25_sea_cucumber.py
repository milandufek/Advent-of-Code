from my_utils import get_data


# https://adventofcode.com/2021/day/25


def get_cucumbers_positions(data: list[str]) -> list[int]:
    rows = len(data)
    cols = len(data[0])
    east = set()
    south = set()
    for r in range(rows):
        for c in range(cols):
            if data[r][c] == '>':
                east.add((r, c))
            elif data[r][c] == 'v':
                south.add((r, c))

    return east, south


def solve(data: list[str]) -> int:
    rows = len(data)
    cols = len(data[0])
    east, south = get_cucumbers_positions(data)
    steps = 0

    while True:
        steps += 1
        all = east | south
        new_east = set()
        for r, c in east:
            new = (r, (c + 1) % cols)
            if new in all:
                new_east.add((r, c))
            else:
                new_east.add(new)

        east_blocked = new_east == east
        east = new_east

        all = east | south
        new_south = set()
        for r, c in south:
            new = ((r + 1) % rows, c)
            if new in all:
                new_south.add((r, c))
            else:
                new_south.add(new)

        south_blocked = new_south == south
        south = new_south

        if east_blocked and south_blocked:
            return steps


if __name__ == '__main__':
    # data_input = get_data('inputs/25_example.in')
    data_input = get_data('inputs/25.in')
    print(f'Score: {solve(data_input)}')
