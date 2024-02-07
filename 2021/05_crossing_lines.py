import re


with open('inputs/05.in') as f:
# with open('inputs/05_example.in') as f:
    lines = f.readlines()

nums = re.compile(r'\d+')


def part_1():
    coordinates = {}
    for line in lines:
        x1, y1, x2, y2 = map(int, nums.findall(line))

        if all((x1 != x2, y1 != y2)):
            continue

        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                point = (x, y)
                coordinates[point] = coordinates.get(point, 0) + 1

    cross = len([c for c in coordinates.values() if c > 1])

    print(f'#1: {cross}')


def part_2():
    coordinates = {}
    for line in lines:
        x1, y1, x2, y2 = map(int, nums.findall(line))

        dx = x2 - x1
        dx = dx // max(1, abs(dx))

        dy = y2 - y1
        dy = dy // max(1, abs(dy))

        x = x1
        y = y1

        while True:
            coordinates[(x, y)] = coordinates.get((x, y), 0) + 1

            if x == x2 and y == y2:
                break

            x += dx
            y += dy

    cross = len([c for c in coordinates.values() if c > 1])

    print(f'#2: {cross}')


if __name__ == '__main__':
    part_1()
    part_2()
