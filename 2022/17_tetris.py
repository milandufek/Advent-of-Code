from itertools import cycle
from my_utils import get_data


# https://adventofcode.com/2022/day/17


class Tetris:

    def __init__(self, input_file: str) -> None:
        self.input_file = input_file
        self.SHAPES = [
            {(0, 0), (1, 0), (2, 0), (3, 0)},  # straight
            {(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)},  # cross
            {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)},  # reversed L
            {(0, 0), (0, 1), (0, 2), (0, 3)},  # I
            {(0, 0), (1, 0), (0, 1), (1, 1)},  # box
        ]
        self.rocks = cycle(self.SHAPES)
        self.jets = cycle(
            [-1 if x == '<' else 1 for x in get_data(self.input_file)[0]])
        self.solid = {(x, -1) for x in range(7)}
        self.height = 0

    def get_rock(self) -> set:
        rock = next(self.rocks)
        return {(x + 2, y + self.height + 3) for x, y in rock}

    def run(self, max_rocks: int = 2022) -> None:
        rested = 0
        rock = self.get_rock()

        for jet in self.jets:
            moved = {(x + jet, y) for x, y in rock}

            if all(0 <= x < 7 for x, y in moved) and not moved & self.solid:
                rock = moved

            moved = {(x, y - 1) for x, y in rock}

            if moved & self.solid:
                self.solid |= rock
                rested += 1
                self.height = max(y for x, y in self.solid) + 1

                if rested == max_rocks:
                    break

                rock = self.get_rock()
            else:
                rock = moved

        print(f'Rested rocks ({rested}) height: {self.height}')


if __name__ =='__main__':
    # t = Tetris('inputs/17_example.in')
    t = Tetris('inputs/17.in')
    t.run()
