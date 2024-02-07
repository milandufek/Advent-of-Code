from utils import get_data


# https://adventofcode.com/2022/day/

def move(position: list, direction: str) -> list:
    match direction:
        case 'L':
            position[0] -= 1
        case 'R':
            position[0] += 1
        case 'U':
            position[1] += 1
        case 'D':
            position[1] -= 1

    return position


def follow(head: list, tail: list) -> list:
    x_diff = head[0] - tail[0]
    y_diff = head[1] - tail[1]

    if abs(x_diff) == 2 and abs(y_diff) == 2:
        tail[0] += x_diff // 2
        tail[1] += y_diff // 2
    else:
        if abs(x_diff) == 2:
            tail[0] += x_diff // 2
            tail[1] = head[1]
        elif abs(y_diff) == 2:
            tail[0] = head[0]
            tail[1] += y_diff // 2

    return tail


def show_visited_positions(moves: list, rope_len: int) -> None:
    last_tail_history = set()
    rope = [[0, 0] for _ in range(rope_len)]

    for instruction in moves:
        direction, steps = instruction.split()
        steps = int(steps)
        rope_len = len(rope)

        for _ in range(steps):  # all steps in one direction
            rope[0] = move(rope[0], direction)  # head moves
            for i in range(1, rope_len):  # then each tail...
                rope[i] = follow(rope[i - 1], rope[i])
                last_tail_history.add(tuple(rope[rope_len - 1]))

    print(f'Rope length ({rope_len}): {len(last_tail_history)}')


if __name__ == '__main__':
    example = [
        'R 4',
        'U 4',
        'L 3',
        'D 1',
        'R 4',
        'D 1',
        'L 5',
        'R 2',
    ]
    large_example = [
        'R 5',
        'U 8',
        'L 8',
        'D 3',
        'R 17',
        'D 10',
        'L 25',
        'U 20',
    ]
    data = get_data('inputs/09.in')
    # show_visited_positions(example, 2)
    show_visited_positions(large_example, 10)
    show_visited_positions(data, 10)
    show_visited_positions(data, 30)
