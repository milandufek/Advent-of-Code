from my_utils import get_data


# https://adventofcode.com/2022/day/8

class Tree:

    def __init__(self, x, y, forest) -> None:
        self.x = x
        self.y = y
        self.forest = forest
        self.x_len = len(self.forest[0])
        self.y_len = len(forest)
        self.value = self.forest[self.y][self.x]

    def is_on_edge(self):
        return self.x == 0 or \
               self.y == 0 or \
               self.x == self.x_len - 1 or \
               self.y == self.y_len - 1

    def get_row(self) -> str:
        return self.forest[self.y]

    def get_column(self) -> list:
        column = []
        for row in self.forest:
            column.append(row[self.x])

        return column

    def is_visible_in_row(self) -> bool:
        row = self.get_row()
        left = row[:self.x + 1]
        top_from_left = max(left) == self.value and left.count(self.value) == 1
        right = row[self.x:]
        top_from_right = max(right) == self.value and right.count(self.value) == 1

        return top_from_left or top_from_right

    def is_visible_in_column(self) -> bool:
        col = self.get_column()
        up = col[:self.y + 1]
        top_from_up = max(up) == self.value and up.count(self.value) == 1
        down = col[self.y:]
        top_from_down =  max(down) == self.value and down.count(self.value) == 1

        return top_from_up or top_from_down

    def is_visible(self) -> bool:
        return self.is_visible_in_column() or self.is_visible_in_row()

    def get_score_left(self):
        row = self.get_row()
        left = row[:self.x + 1]
        data = [x for x in reversed(left)]
        return self.evaluate_score(data)

    def get_score_right(self):
        row = self.get_row()
        right = row[self.x:]
        data = [x for x in right]
        return self.evaluate_score(data)

    def get_score_up(self):
        col = self.get_column()
        up = col[:self.y + 1]
        data = [x for x in reversed(up)]
        return self.evaluate_score(data)

    def get_score_down(self):
        col = self.get_column()
        down = col[self.y:]
        data = [x for x in down]
        return self.evaluate_score(data)

    def evaluate_score(self, view):
        score = []
        trees_in_row = len(view)
        for i, val in enumerate(view, start=1):
            if i == 1:
                continue
            elif val < self.value or i == trees_in_row:
                score.append(1)
            else:
                score.append(1)
                break

        return sum(score)

    def get_scenic_score(self) -> int:
        return self.get_score_left() * self.get_score_right() *\
            self.get_score_up() * self.get_score_down()


def count(forest):
    x_len = len(forest[0])
    y_len = len(forest)
    count_visible = 0
    scores = []
    for y in range(y_len):
        for x in range(x_len):
            tree = Tree(x, y, forest)
            if tree.is_visible():
                count_visible += 1
            scores.append(tree.get_scenic_score())

    print(f'Visible: {count_visible}\nMost scenic: {max(scores)}')


if __name__ == '__main__':
    example = [
        '30373',
        '25512',
        '65332',
        '33549',
        '35390',
    ]
    # count(example)
    data = get_data('inputs/08.in')
    count(data)
