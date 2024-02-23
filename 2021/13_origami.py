# https://adventofcode.com/2021/day/13


def parse_input(file_name: str) -> tuple[set[tuple[int, int]], list[tuple[str, int]]]:
    with open(file_name) as f:
        coordinates, instructions = f.read().split('\n\n')

    points = set()
    for p in coordinates.splitlines():
        x, y = tuple(map(int, p.split(',')))
        points.add((x, y))

    folds = []
    for i in instructions.splitlines():
        axis, line = i.split()[-1].split('=')
        folds.append((axis, int(line)))

    return points, folds


def print_grid(points: set) -> None:
    max_x = max(x for x, _ in points)
    max_y = max(y for _, y in points)
    for y in range(max_y + 1):
        print(''.join('🟩' if (x, y) in points else '⬛' for x in range(max_x + 1)))


def fold(points: set[tuple[int, int]], axis: str, line: int) -> set[tuple[int, int]]:
    assert axis in ('x', 'y'), f'Invalid axis: {axis = }'
    # print(f'\nFolding on {axis = } at {line = }\n')

    if axis == 'y':
        return {(x, line - (y - line) if y > line else y) for x, y in points}

    return {(line - (x - line) if x > line else x, y) for x, y in points}


def solve(_input_file: str, part: int = 1) -> int:
    points, folds = parse_input(_input_file)

    for axis, line in folds:
        points = fold(points, axis, line)

        if part == 1:
            return len(points)

    print_grid(points)

    return None


if __name__ == '__main__':
    example = 'inputs/13_example.in'
    data_input = 'inputs/13.in'
    print(f'Score #1: {solve(data_input)}')
    print('Part #2:')
    solve(data_input, 2)
