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
        self.jet_pattern = [-1 if x == '<' else 1 for x in get_data(self.input_file)[0]]
        self.jets = cycle(self.jet_pattern)
        self.solid = {(x, -1) for x in range(7)}
        self.height = 0
        self.height_offset = 0
        self.seen = {}

    def get_rock(self) -> set:
        rock = next(self.rocks)
        return {(x + 2, y + self.height + 3) for x, y in rock}

    def get_fingerprint(self, rock_index: int, jet_index: int) -> tuple:
        window = 50
        surface = frozenset(
            (x, y - self.height) for x, y in self.solid
            if y >= self.height - window)
        return (rock_index, jet_index, surface)

    def run(self, max_rocks: int = 2022) -> int:
        rested = 0
        rock = self.get_rock()

        for i, jet in enumerate(self.jets):
            moved = {(x + jet, y) for x, y in rock}

            if all(0 <= x < 7 for x, _ in moved) and not moved & self.solid:
                rock = moved

            moved = {(x, y - 1) for x, y in rock}

            if moved & self.solid:
                self.solid |= rock
                rested += 1
                self.height = max(y for _, y in self.solid) + 1

                if rested == max_rocks:
                    break

                if self.seen is not None:
                    rock_index = rested % len(self.SHAPES)
                    jet_index = (i + 1) % len(self.jet_pattern)
                    fingerprint = self.get_fingerprint(rock_index, jet_index)

                    if fingerprint in self.seen:
                        cycle_start_rested, cycle_start_height = self.seen[fingerprint]
                        cycle_length = rested - cycle_start_rested
                        height_gain = self.height - cycle_start_height
                        num_cycles = (max_rocks - rested) // cycle_length

                        self.height_offset += num_cycles * height_gain
                        rested += num_cycles * cycle_length
                        self.seen = None

                        if rested == max_rocks:
                            break
                    else:
                        self.seen[fingerprint] = (rested, self.height)

                rock = self.get_rock()
            else:
                rock = moved

        total_height = self.height + self.height_offset
        print(f'Rested rocks ({rested}) height: {total_height}')
        return total_height


if __name__ =='__main__':
    t = Tetris('inputs/17.in')
    t.run(2022)
    t2 = Tetris('inputs/17.in')
    t2.run(1_000_000_000_000)
