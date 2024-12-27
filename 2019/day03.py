from my_utils import get_data


# https://adventofcode.com/2019/day/3


def get_wire_path(wire: list[str]) -> list[tuple[int, int]]:
    path = []
    x, y = 0, 0
    for move in wire:
        direction = move[0]
        steps = int(move[1:])
        for _ in range(steps):
            match direction:
                case 'R': x += 1
                case 'L': x -= 1
                case 'U': y += 1
                case 'D': y -= 1
                case _: raise ValueError(f'Invalid direction: {direction}')
            path.append((x, y))

    return path


def solve(data: list[str]) -> None:
    a = data[0].split(',')
    b = data[1].split(',')
    path_a = get_wire_path(a)
    path_b = get_wire_path(b)
    intersections = set(path_a) & set(path_b)
    print('#1', min(abs(x) + abs(y) for x, y in intersections))
    print('#2', min(path_a.index(i) + path_b.index(i) for i in intersections) + 2)


if __name__ == '__main__':
    data_input = get_data('inputs/03.txt')
    solve(data_input)
