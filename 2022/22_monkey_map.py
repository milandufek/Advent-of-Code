import re
from collections import deque
from typing import List
from my_utils import get_data


# https://adventofcode.com/2022/day/22


class MonkeyMap:

    def __init__(self, input_file: str) -> None:
        self.input_file = input_file
        self.space: List[str] = []
        self.moves: list = []
        self.current_xy = None
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
        score = {'>': 0, 'v': 1, '<': 2, '^': 3,}
        col, row = self.current_xy
        s = 1000 * (row + 1)  + 4 * (col + 1) + score[self.direction]

        print(f'Score #1 ({self.input_file}): {s}')

    def rotate(self, side: str) -> None:
        d = deque(['>', 'v', '<', '^'])
        current = d.index(self.direction)

        if side == 'R':
            d.rotate(len(d) - 1)
        elif side == 'L':
            d.rotate()
        else:
            raise NotImplementedError(f"Rotation not implemented for '{side}'")

        self.direction = d[current]

    def main(self) -> None:
        self.parse_input()
        self.current_xy = (self.space[0].index('.'), 0)

        for m in self.moves:

            if isinstance(m, str):
                self.rotate(m)
                continue

            match self.direction:
                case '>':
                    self.move_right(m)
                case '<':
                    self.move_left(m)
                case 'v':
                    self.move_down(m)
                case '^':
                    self.move_up(m)

        self.show_password()


if __name__ == '__main__':
    mme = MonkeyMap('inputs/22_example.in')
    mme.main()
    mm = MonkeyMap('inputs/22.in')
    mm.main()
