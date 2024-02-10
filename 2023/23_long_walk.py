from my_utils import get_data


# https://adventofcode.com/2023/day/23


class Maze:

    def __init__(self, grid: list) -> None:
        self.grid = grid
        self.end = (len(grid) - 1, grid[-1].index('.'))
        self.start = (0, grid[0].index('.'))
        self.points = {self.start, self.end}
        self.graph = {}
        self.seen = set()
        self.directions = {}

    def get_points(self) -> set:
        for r, row in enumerate(self.grid):
            for c, ch in enumerate(row):
                if ch == '#':
                    continue

                adjacent = 0
                for ar, ac in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if self.is_there_a_way(ar, ac):
                        adjacent += 1

                if adjacent >= 3:
                    self.points.add((r, c))

        return self.points

    def get_longest_path(self, part: int = 1) -> int:
        self.set_directions(part)
        self.generate_graph()
        longest_path = self.dfs(self.start)

        return longest_path

    def generate_graph(self) -> None:
        self.points |= self.get_points()
        self.graph = {p: {} for p in self.points}

        for start_point in self.points:
            stack = [(*start_point, 0)]
            seen = {*start_point}

            while stack:
                r, c, distance = stack.pop()

                if distance != 0 and (r, c) in self.points:
                    self.graph[*start_point][(r, c)] = distance
                    continue

                tile = self.grid[r][c]
                for dr, dc in self.directions[tile]:
                    point = (r + dr, c + dc)

                    if self.is_there_a_way(*point) and point not in seen:
                        stack.append((*point, distance + 1))
                        seen.add(point)

    def is_there_a_way(self, r: int, c: int) -> bool:
        return (
            0 <= r < len(self.grid)
            and 0 <= c < len(self.grid[0])
            and self.grid[r][c] != '#'
        )

    def dfs(self, point: tuple) -> int:
        if point == self.end:
            return 0

        max_distance = -float('inf')
        self.seen.add(point)

        for nx in self.graph[point]:
            if nx not in self.seen:
                max_distance = max(max_distance, self.dfs(nx) + self.graph[point][nx])

        self.seen.remove(point)

        return max_distance

    def set_directions(self, part: int) -> None:
        all_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        if part == 1:
            self.directions = {
                '.': all_directions,
                '^': [(-1, 0)],
                'v': [(1, 0)],
                '<': [(0, -1)],
                '>': [(0, 1)],
            }
        else:
            self.directions = {
                '.': all_directions,
                '^': all_directions,
                'v': all_directions,
                '<': all_directions,
                '>': all_directions,
            }


if __name__ == '__main__':
    example = get_data('inputs/23_example.in')
    maze_ex = Maze(example)
    print(f'Example #1: {maze_ex.get_longest_path(1)}')
    print(f'Example #2: {maze_ex.get_longest_path(2)}')

    data = get_data('inputs/23.in')
    maze = Maze(data)
    print(f'Score #1: {maze.get_longest_path(1)}')
    print(f'Score #2: {maze.get_longest_path(2)}')
