import re
from typing import List
from utils import get_data


# https://adventofcode.com/2022/day/22


class MonkeyMap:

    def __init__(self, input_file: str, start: tuple) -> None:
        self.input_file = input_file
        self.space: List[list] = []
        self.moves: list = []
        self.current_xy = start
        self.direction = '>'

    def parse_input(self) -> None:
        input_data = get_data(self.input_file)
        max_length = len(max(input_data[:-2], key=len))

        for line in input_data:
            if not line:
                break

            length = len(line)
            if length < max_length:
                line += (max_length - length) * ' '

            self.space.append(line.replace(' ', 'x'))

        for m in re.findall(r'\d+|\w', input_data[-1]):
            if m.isdigit():
                self.moves.append(int(m))
            else:
                self.moves.append(m)

    def move_right(self, steps: int) -> None:
        x, y = self.current_xy
        row = self.space[y]

        for _ in range(steps):
            x += 1
            if x >= len(row) or row[x] == 'x':
                tmp_x = row.index('.')
                if tmp_x > 0 and row[tmp_x - 1] == '#':
                    x -= 1
                    break

                x = tmp_x
                continue

            if row[x] == '#':
                x -= 1
                break

        self.current_xy = (x, y)

    def move_left(self, steps: int) -> None:
        x, y = self.current_xy
        row = self.space[y]

        for _ in range(steps):
            x -= 1
            if x < 0 or row[x] == 'x':
                tmp_x = row.rindex('.')
                if tmp_x < len(row) - 1 and row[tmp_x + 1] == '#':
                    x += 1
                    break

                x = tmp_x
                continue

            if row[x] == '#':
                x += 1
                break

        self.current_xy = (x, y)

    def move_down(self, steps: int) -> None:
        x, y = self.current_xy
        col = ''.join([r[x] for r in self.space])

        for _ in range(steps):
            y += 1
            if y >= len(col) or col[y] == 'x':
                tmp_y = col.index('.')
                if tmp_y > 0 and col[tmp_y - 1] == '#':
                    y -= 1
                    break

                y = tmp_y
                continue

            if col[y] == '#':
                y -= 1
                break

        self.current_xy = (x, y)

    def move_up(self, steps: int) -> None:
        x, y = self.current_xy
        col = ''.join([r[x] for r in self.space])

        for _ in range(steps):
            y -= 1
            if y < 0 or col[y] == 'x':
                tmp_y = col.rindex('.')
                if tmp_y < len(col) - 1 and col[tmp_y + 1] == '#':
                    y += 1
                    break

                y = tmp_y
                continue

            if col[y] == '#':
                y += 1
                break

        self.current_xy = (x, y)

    def show_password(self) -> None:
        scores = {'>': 0, 'v': 1, '<': 2, '^': 3,}
        col, row = self.current_xy
        s = 1000 * (row + 1)  + 4 * (col + 1) + scores[self.direction]

        print(f'Score #1 ({self.input_file}): {s}')

    def rotate(self, side: str):
        d = ['>', 'v', '<', '^']
        if side == 'R':
            if d.index(self.direction) == 3:
                self.direction = d[0]
            else:
                self.direction = d[d.index(self.direction) + 1]
        elif side == 'L':
            if d.index(self.direction) == 0:
                self.direction = d[-1]
            else:
                self.direction = d[d.index(self.direction) - 1]

    def main(self):
        self.parse_input()
        for i in self.moves:
            if isinstance(i, str):
                self.rotate(i)
                continue

            match self.direction:
                case '>':
                    self.move_right(i)
                case '<':
                    self.move_left(i)
                case 'v':
                    self.move_down(i)
                case '^':
                    self.move_up(i)

        self.show_password()


if __name__ == '__main__':
    mme = MonkeyMap('inputs/22_example.in', start=(8, 0))
    mme.main()
    mm = MonkeyMap('inputs/22.in', start=(49, 0))
    mm.main()
