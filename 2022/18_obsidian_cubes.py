from collections import deque
from functools import cache
from my_utils import get_data


# https://adventofcode.com/2022/day/18


class Obsidian:

    def __init__(self, input_file: str) -> None:
        self.input_file = input_file
        self.cubes: list = []
        self.DELTAS: list = [
            (1, 0, 0), (-1, 0, 0),
            (0, 1, 0), (0, -1, 0),
            (0, 0, 1), (0, 0, -1)
        ]
        self.min_x = self.max_x = 0
        self.min_y = self.max_y = 0
        self.min_z = self.max_z = 0

    def parse_data(self) -> None:
        for line in get_data(self.input_file):
            x, y, z = map(int, line.split(','))
            cube = (x, y, z)
            self.cubes.append(cube)

    def calc_min_max(self) -> None:
        self.min_x = min(self.cubes, key=lambda x: x[0])[0]
        self.max_x = max(self.cubes, key=lambda x: x[0])[0]
        self.min_y = min(self.cubes, key=lambda x: x[1])[1]
        self.max_y = max(self.cubes, key=lambda x: x[1])[1]
        self.min_z = min(self.cubes, key=lambda x: x[2])[2]
        self.max_z = max(self.cubes, key=lambda x: x[2])[2]

    def approx_surface(self) -> None:
        surface = 0
        exterior_only = 0

        self.parse_data()
        self.calc_min_max()

        for cube in self.cubes:
            x, y, z = cube
            for dx, dy, dz in self.DELTAS:
                neighbor_cube = (x + dx, y + dy, z + dz)

                if neighbor_cube not in self.cubes:
                    surface += 1

                if self.reach_out(neighbor_cube):
                    exterior_only += 1

        print(f'Surface #1: {surface}')
        print(f'Surface #2: {exterior_only}')

    @cache
    def reach_out(self, cube: tuple) -> bool:
        q = deque()
        q.append(cube)
        seen = set()

        while q:
            x, y, z = q.popleft()

            if (x, y, z) in seen:
                continue

            seen.add((x, y, z))

            if (x, y, z) in self.cubes:
                continue

            if (self.min_x > x < self.max_x or \
                self.min_y > y < self.max_y or \
                self.min_z > z < self.max_z):
                return True

            for dx, dy, dz in self.DELTAS:
                q.append((x + dx, y + dy, z + dz))

        return False


if __name__ == '__main__':
    # oc = Obsidian('inputs/18_example.in')
    oc = Obsidian('inputs/18.in')
    oc.approx_surface()
