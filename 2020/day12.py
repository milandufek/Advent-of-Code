from dataclasses import dataclass


# https://adventofcode.com/2020/day/12


def get_data(file_path: str) -> list[str]:
    with open(file_path) as f:
        return f.readlines()

@dataclass
class Point:
    x: int
    y: int


def solve_1(data: list[str]) -> int:
    ship = Point(0, 0)
    directions = {'E': (1, 0), 'N': (0, 1), 'W': (-1, 0), 'S': (0, -1)}
    angles = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}
    angle = 0
    for line in data:
        action = line[0]
        step = int(line[1:])

        if action in directions:
            dx, dy = directions[action]
            ship.x += dx * step
            ship.y += dy * step
        elif action == 'R':
            angle = (angle - step) % 360
        elif action == 'L':
            angle = (angle + step) % 360
        else:
            dx, dy = directions[angles[angle]]
            ship.x += dx * step
            ship.y += dy * step

    return abs(ship.x) + abs(ship.y)


def solve_2(data: list[str]) -> int:
    ship = Point(0, 0)
    waypoint = Point(10, 1)
    directions = {'E': (1, 0), 'N': (0, 1), 'W': (-1, 0), 'S': (0, -1)}
    for line in data:
        action = line[0]
        step = int(line[1:])

        if action in directions:
            dx, dy = directions[action]
            waypoint.x += dx * step
            waypoint.y += dy * step
        elif action == 'R':
            for _ in range(step // 90):
                waypoint.x, waypoint.y = waypoint.y, -waypoint.x
        elif action == 'L':
            for _ in range(step // 90):
                waypoint.x, waypoint.y = -waypoint.y, waypoint.x
        else:
            ship.x += waypoint.x * step
            ship.y += waypoint.y * step

    return abs(ship.x) + abs(ship.y)


if __name__ == '__main__':
    # data_input = get_data('inputs/test.txt')
    data_input = get_data('inputs/12.txt')
    print(f'#1: {solve_1(data_input)}')
    print(f'#2: {solve_2(data_input)}')
