from itertools import cycle
from my_utils import get_data


# https://adventofcode.com/2022/day/17


class Tetris:

    def __init__(self, input_file: str) -> None:
        self.input_file = input_file
        self.SHAPES = [
            {0, 1, 2, 3},  # straight
            {1, 1j, 1 + 1j, 2 + 1j, 1 + 2j},  # cross
            {0, 1, 2, 2 + 1j, 2 + 2j},  # reversed L
            {0, 1j, 2j, 3j},  # I
            {0, 1, 1j, 1 + 1j},  # box
        ]
        self.rocks = cycle(self.SHAPES)
        self.jets = cycle(
            [-1 if x == '<' else 1 for x in get_data(self.input_file)[0]])
        self.solid = {x - 1j for x in range(7)}
        self.height = 0

    def get_rock(self) -> set:
        rock = next(self.rocks)
        return {x + 2 + ((self.height + 3) * 1j) for x in rock}

    def run(self, max_rocks: int = 2022) -> None:
        rested = 0
        rock = self.get_rock()

        for jet in self.jets:
            moved = {x + jet for x in rock}

            if all(0 <= x.real < 7 for x in moved) and not moved & self.solid:
                rock = moved

            moved = {x - 1j for x in rock}

            if moved & self.solid:
                self.solid |= rock
                rested += 1
                self.height = max(x.imag for x in self.solid) + 1

                if rested == max_rocks:
                    break

                rock = self.get_rock()
            else:
                rock = moved

        print(f'Rested rocks ({rested}) height: {int(self.height)}')


if __name__ =='__main__':
    # t = Tetris('inputs/17_example.in')
    t = Tetris('inputs/17.in')
    t.run()
