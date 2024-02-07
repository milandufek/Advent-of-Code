from functools import cache
from my_utils import get_data


# https://adventofcode.com/2022/day/16


class Dungeon:

    def __init__(self, input: str) -> None:
        self.input = input
        self.flows = {}
        self.knots = {}
        self.START = 'AA'

    def parse_data(self) -> None:
        for line in get_data(self.input):
            cols = line.split()
            valve = cols[1]
            flow = int(cols[4].split('=')[1].strip(';'))
            self.flows[valve] = flow
            self.knots[valve] = [x.strip().strip(',') for x in cols[9:]]

    @cache
    def dfs(self, pos: str, time: int, opened: frozenset, wait=False) -> int:
        if time == 0:
            if wait:
                return self.dfs(self.START, 26, opened)
            return 0

        score = max([self.dfs(n, time - 1, opened, wait) for n in self.knots[pos]])

        if self.flows[pos] > 0 and pos not in opened:
            next = set(opened)
            next.add(pos)
            next = frozenset(next)  # due to cache
            score = max(
                score,
                (time - 1) * self.flows[pos] + self.dfs(pos, time - 1, next, wait),
            )

        return score

    def run(self) -> None:
        self.parse_data()

        part_1 = self.dfs(self.START, 30, frozenset())
        print(f'Part #1: {part_1}')

        part_2 = self.dfs(self.START, 26, frozenset(), True)
        print(f'Part #2: {part_2}')


if __name__ == '__main__':
    # d = Dungeon('inputs/16_example.in')
    d = Dungeon('inputs/16.in')
    d.run()
