import heapq


def get_position(grid: list, char: str) -> tuple[int, int]:
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == char:
                return r, c


def solve() -> None:
    sr, sc = get_position(grid, 'S')
    er, ec = get_position(grid, 'E')
    queue = [(0, sr, sc, 0, 1)]
    seen = {(sr, sc, 0, 1)}

    while queue:
        cost, r, c, dr, dc = heapq.heappop(queue)
        seen.add((r, c, dr, dc))

        if r == er and c == ec:
            print('Cons:', cost)
            break

        directions = [
            (cost + 1, r + dr, c + dc, dr, dc),  # Move forward
            (cost + 1000, r, c, dc, -dr),        # Turn right
            (cost + 1000, r, c, -dc, dr),        # Turn left
        ]

        for new_cost, nr, nc, ndr, ndc in directions:
            if grid[nr][nc] == '#':
                continue
            if (nr, nc, ndr, ndc) in seen:
                continue
            heapq.heappush(queue, (new_cost, nr, nc, ndr, ndc))


if __name__ == '__main__':
    with open('inputs/16.txt') as f:
        grid = [list(line.strip()) for line in f]
    solve()
