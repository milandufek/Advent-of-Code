# https://adventofcode.com/2016/day/1


def prase_input(file: str) -> list[str]:
    with open(file) as f:
        return f.read().strip().split(', ')


def turn(direction: str, facing: int) -> int:
    # return: new facing direction
    #  0 = N
    #  1 = E
    #  2 = S
    #  3 = W
    if direction == 'R':
        return (facing + 1) % 4
    return (facing - 1) % 4


def solve_1(instructions: list[str]) -> int:
    x, y = 0, 0
    facing = 0

    for i in instructions:
        direction, steps = i[0], int(i[1:])
        facing = turn(direction, facing)

        match facing:
            case 0:
                y += steps
            case 1:
                x += steps
            case 2:
                y -= steps
            case 3:
                x -= steps

    return abs(x) + abs(y)


def solve_2(instructions: list[str]) -> int:
    x, y = 0, 0
    facing = 0
    visited = set()

    for i in instructions:
        direction, steps = i[0], int(i[1:])
        facing = turn(direction, facing)

        for _ in range(steps):
            match facing:
                case 0:
                    y += 1
                case 1:
                    x += 1
                case 2:
                    y -= 1
                case 3:
                    x -= 1

            if (x, y) in visited:
                return abs(x) + abs(y)

            visited.add((x, y))

    return -1


if __name__ == '__main__':
    _input_data = prase_input('inputs/01.in')
    print(f'Part 1: {solve_1(_input_data)}')
    print(f'Part 2: {solve_2(_input_data)}')
