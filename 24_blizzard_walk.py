from collections import deque
from functools import cache
from utils import get_data


# https://adventofcode.com/2022/day/24


class Blizzard:

    def __init__(self, input_file: str) -> None:
        self.input_file: str = input_file
        self.DIRECTIONS: dict = {
            '<': (0, -1),
            '>': (0, 1),
            '^': (-1, 0),
            'v': (1, 0),
        }

    def parse_data(self) -> None:
        self.lines = get_data(self.input_file)
        # exclude walls
        self.nr = len(self.lines) - 2
        self.nc = len(self.lines[0]) - 2
        self.start = (-1, self.lines[0].index('.') - 1)
        self.end = (self.nr, self.lines[-1].index('.') - 1)

    @cache
    def get_blizzard(self, time: int) -> list:
        blizzard = set()
        for r, row in enumerate(self.lines[1:-1]):
            for c, char in enumerate(row[1:-1]):
                if char in '<>^v':
                    dr, dc = self.DIRECTIONS[char]
                    blizzard.add(
                        ((r + dr * time) % self.nr, (c + dc * time) % self.nc)
                    )

        return blizzard

    def bfs(self):
        q = deque()
        q.append((0, *self.start))
        seen = set()

        while True:
            time, r, c = q.popleft()

            if (time, r, c) in seen:
                continue

            seen.add((time, r, c))
            time += 1
            blizzard = self.get_blizzard(time)

            if (r, c) not in blizzard:
                q.append((time, r, c))

            for dr, dc in self.DIRECTIONS.values():
                # check if possible to reach end
                if (r + dr, c + dc) == self.end:
                    print(f'Part #1: {time}')
                    exit(0)

                # check possible next positions
                if 0 <= r + dr < self.nr and 0 <= c + dc < self.nc:
                    if (r + dr, c + dc) not in blizzard:
                        q.append((time, r + dr, c + dc))

    def run(self):
        self.parse_data()
        self.bfs()


if __name__ == '__main__':
    # b = Blizzard('inputs/24_example.in')
    b = Blizzard('inputs/24.in')
    b.run()
