from my_utils import get_data


# https://adventofcode.com/2023/day/18


def get_direction_coordinates(direction: str) -> tuple[int, int]:
    match direction:
        case 'R' | 0:
            return 1, 0
        case 'L' | 2:
            return -1, 0
        case 'U' | 3:
            return 0, 1
        case 'D' | 1:
            return 0, -1


def perimeter(points: list[tuple[int, int]]) -> int:
    total = 0
    shifted_points = points[1:] + [points[0]]

    for (r1, c1), (r2, c2) in zip(points, shifted_points):
        total += abs(r1 - r2) + abs(c1 - c2)

    return total


def internal_area(points: list[tuple[int, int]]) -> int:
    # https://en.wikipedia.org/wiki/Shoelace_formula
    total = 0
    shifted_points = points[1:] + [points[0]]

    for (r1, c1), (r2, c2) in zip(points, shifted_points):
        total += (r1 + r2) * (c1 - c2)

    return total // 2


def parse_line(line: str, part: int = 1) -> tuple[str, int, str]:
    if part == 2:
        _, hex_val = line.split('#')
        hex_val = hex_val.strip(')')
        direction, length = int(hex_val[-1]), int(hex_val[:-1], 16)
    else:
        direction, length, _ = line.split()
        length = int(length)

    return direction, length


def solve(_input: list[str], part: int = 1) -> int:
    r, c = 0, 0
    points = [(r, c)]

    for line in _input:
        direction, length = parse_line(line, part)
        dr, dc = get_direction_coordinates(direction)
        r += dr * length
        c += dc * length
        points.append((r, c))

    # https://en.wikipedia.org/wiki/Pick%27s_theorem
    return internal_area(points) + perimeter(points) // 2 + 1


if __name__ == '__main__':
    example = get_data('inputs/18_example.in')
    data_input = get_data('inputs/18.in')
    print(f'Example #1: {solve(example)}')
    print(f'Score #1: {solve(data_input)}')
    print(f'Example #2: {solve(example, 2)}')
    print(f'Score #2: {solve(data_input, 2)}')
