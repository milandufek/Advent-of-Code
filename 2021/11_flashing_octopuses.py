# https://adventofcode.com/2021/day/11


class FlashingOctopuses:

    def __init__(self, input_file: str) -> None:
        self.input_file = input_file
        self.grid = self.parse_input()
        self.score_1, self.score_2 = 0, 0
        self.flashes = []

    def parse_input(self) -> list:
        with open(self.input_file) as f:
            grid = [list(map(int, line))
                    for line in f.read().splitlines()]

        return grid

    def flash(self, r: int, c: int) -> None:
        self.score_1 += 1

        if self.flashes:
            self.flashes[r][c] += 1

        for ar in range(r - 1, r + 2):
            for ac in range(c - 1, c + 2):
                if ar == r and ac == c:
                    continue

                if 0 <= ar < len(self.grid) and 0 <= ac < len(self.grid[ar]):
                    self.grid[ar][ac] += 1

                    if self.grid[ar][ac] == 10:
                        self.flash(ar, ac)
                        self.grid[ar][ac] += 1

    def step(self) -> None:
        for r, row in enumerate(self.grid):
            for c, _ in enumerate(row):
                self.grid[r][c] += 1

                if self.grid[r][c] == 10:
                    self.flash(r, c)
                    self.grid[r][c] += 1

        # Set energy level of flashed octopuses to 0.
        for r, row in enumerate(self.grid):
            for c, _ in enumerate(row):
                if self.grid[r][c] > 9:
                    self.grid[r][c] = 0

    def solve_1(self) -> int:
        self.grid = self.parse_input()

        for _ in range(100):
            self.step()

        print(f'Score #1: {self.score_1}')

    def solve_2(self) -> None:
        self.grid = self.parse_input()
        self.flashes = [[0] * len(x) for x in self.grid]

        while True:
            self.score_2 += 1
            self.step()

            if all(map(all, self.flashes)):
                print(f'Score #2: {self.score_2}')
                break

            self.flashes = [[0] * len(x) for x in self.grid]


if __name__ == '__main__':
    example = 'inputs/11_example.in'
    foe = FlashingOctopuses(example)
    foe.solve_1()
    foe.solve_2()

    data_input = 'inputs/11.in'
    fo = FlashingOctopuses(data_input)
    fo.solve_1()
    fo.solve_2()
