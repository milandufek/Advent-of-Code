from utils import get_data


def parse_line(line: str) -> tuple:
    line = line.split()

    if line[1] == 'off':
        action = 'off'
        x_from, y_from = map(int, line[2].split(','))
        x_to, y_to = map(int, line[4].split(','))
    elif line[1] == 'on':
        action = 'on'
        x_from, y_from = map(int, line[2].split(','))
        x_to, y_to = map(int, line[4].split(','))
    else:
        action = 'toggle'
        x_from, y_from = map(int, line[1].split(','))
        x_to, y_to = map(int, line[3].split(','))

    return action, x_from, y_from, x_to, y_to

def part_1():
    grid = [[False for x in range(1000)] for y in range(1000)]
    for line in get_data('inputs/06.in'):
        action, x_from, y_from, x_to, y_to = parse_line(line)
        for y in range(y_from, y_to + 1):
            for x in range(x_from, x_to + 1):
                if action == 'on':
                    grid[y][x] = True
                elif action == 'off':
                    grid[y][x] = False
                else:
                    grid[y][x] = not grid[y][x]

    turned_on = 0
    for y in grid:
        turned_on += y.count(True)
    print(f'Turned on: {turned_on}')


def part_1_set():
    # nicer but much slower
    lights = set()
    for line in get_data('inputs/06.in'):
        action, x_from, y_from, x_to, y_to = parse_line(line)
        for y in range(y_from, y_to + 1):
            for x in range(x_from, x_to + 1):
                light = (x, y)
                if action == 'on':
                    lights.add(light)
                elif action == 'off':
                    if light in lights:
                        lights.remove(light)
                else:
                    if light in lights:
                        lights.remove(light)
                    else:
                        lights.add(light)

    print(f'Turned on: {len(lights)}')


def part_2():
    grid = [[0 for x in range(1000)] for y in range(1000)]
    for line in get_data('inputs/06.in'):
        action, x_from, y_from, x_to, y_to = parse_line(line)

        for y in range(y_from, y_to + 1):
            for x in range(x_from, x_to + 1):
                if action == 'on':
                    grid[y][x] += 1
                elif action == 'off':
                    if grid[y][x] > 0:
                        grid[y][x] -= 1
                else:
                    grid[y][x] += 2

    brightness = 0
    for y in grid:
        for x in y:
            brightness += x

    print(f'Brightness: {brightness}')


if __name__ == '__main__':
    part_1()
    # part_1_set()
    part_2()
