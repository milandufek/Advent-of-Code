from copy import deepcopy
from typing import Tuple
from utils import get_data, save_picture, create_gif


# https://adventofcode.com/2022/day/14

def parse_data(scan_data: list) -> list:
    coordinates = set()

    for line in scan_data:
        prev_x, prev_y = None, None

        for trace in line.split('->'):
            x, y = map(int, trace.strip().split(','))
            coordinates.add((x, y))

            if y == prev_y:
                if x < prev_x:
                    for i in range(x, prev_x):
                        coordinates.add((i, y))
                elif x >= prev_x:
                    for i in range(prev_x, x):
                        coordinates.add((i, y))

            if x == prev_x:
                if y < prev_y:
                    for i in range(y, prev_y):
                        coordinates.add((x, i))
                elif y >= prev_y:
                    for i in range(prev_y, y):
                        coordinates.add((x, i))

            prev_x = x
            prev_y = y

    return coordinates


class DustSimulator:

    def __init__(self, coordinates: list) -> None:
        self.AIR = '.'
        self.ROCK = '#'
        self.DUST = 'o'
        self.coordinates = coordinates
        self.space = []
        self.sand_hole = (500, 0)
        self.min_x = 0
        self.max_x = 0
        self.x_shift = 0
        self.dust_rested = 0
        self.iteration = 0

    def prepare_space(self, part_2: bool = False) -> None:
        lines = [i[0] for i in self.coordinates]
        self.min_x = min(lines)
        self.max_x = max(lines)
        max_y = max([i[1] for i in self.coordinates])

        self.x_shift = self.min_x

        if part_2:
            max_y += 2
            self.x_shift = 100
            self.space = [[self.AIR for x in range(self.max_x + self.x_shift)]\
                          for y in range(max_y)]
        else:
            self.space = [[self.AIR for x in range(self.max_x - self.min_x + 1)]\
                          for y in range(0, max_y + 1)]

        for xy in self.coordinates:  # add ROCKs
            x = xy[0] - self.x_shift
            y = xy[1]
            self.space[y][x] = self.ROCK

        if part_2:
            bottom = [self.ROCK for x in range(len(self.space[0]))]
            self.space.append(bottom)

    def show_space(self, dy: int, dx: int) -> None:
        print(f'\n#{self.iteration}')
        for y, line in enumerate(self.space):
            if y == dy:
                lc = line.copy()
                lc[dx] = '+'
                print(lc)
            else:
                print(line)

    def run(self, generate_images: bool = False):
        dust_falling = False

        while True:
            if not dust_falling:
                dx, dy = self.sand_hole
                dx -= self.x_shift
                dust_falling = True
                continue

            if generate_images:
                self.space_to_image()

            dust_falling = self.fall(dy, dx)

    def fall(self, dy: int, dx: int) -> bool:
        self.iteration += 1

        # part 1
        if dx < 0 or dx > len(self.space[0]) or dy >= len(self.space) - 1:
            print(f'Rested dust count #1: {self.dust_rested}')
            exit(0)

        # part 2
        if dy == 0 and self.space[dy][dx] == self.DUST:
            print(f'Rested dust count #2: {self.dust_rested}')
            exit(0)

        if self.space[dy + 1][dx] == self.AIR:
            self.fall(dy + 1, dx)
        elif self.space[dy + 1][dx] in (self.DUST, self.ROCK):
            # to left bottom
            if self.space[dy + 1][dx - 1] == self.AIR:
                self.fall(dy + 1, dx - 1)
            # to right bottom
            elif self.space[dy + 1][dx + 1] == self.AIR:
                self.fall(dy + 1, dx + 1)
            else:
                self.space[dy][dx] = self.DUST
                self.dust_rested += 1
                return False

        return True

    def space_to_image(self, name: str = None) -> None:
        if self.iteration % 3 != 0:
            return

        pic_data = []
        snapshot = deepcopy(self.space)
        snapshot[0][self.sand_hole[0] - self.max_x] = '+'

        for y in snapshot:
            line = y.copy()
            for i in range(len(line)):
                if line[i] == '.':
                    line[i] = (128, 128, 128)  # gray
                elif line[i] == 'o':
                    line[i] = (255, 255, 0)  # yellow
                elif line[i] == '#':
                    line[i] = (0, 0, 0)  # black
                elif line[i] == '+':
                    line[i] = (255, 0, 0)  # red
            pic_data.append(line)

        name = name if name else self.iteration
        save_picture(pic_data, name)

if __name__ == '__main__':
    example = [
        '498,4 -> 498,6 -> 496,6',
        '503,4 -> 502,4 -> 502,9 -> 494,9',
    ]
    # ds = DustSimulator(parse_data(example))
    ds = DustSimulator(parse_data(get_data('inputs/14.in')))
    # ds.prepare_space()
    ds.prepare_space(part_2=True)
    ds.run()

    # create_gif('images/14_part_1.gif', fps=50)
