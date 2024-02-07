def get_data(file: str) -> list:
    with open(file) as f:
        return f.readlines()


def solve(dist, vert):
    INF = int('inf+')
    for p in range(vert):
        for q in range(vert):
            if(dist[p][q] == INF):
                print("INF", end=" ")
            else:
                print(dist[p][q], end="  ")
        print(" ")


def floyd_warshall(graph: dict, vert: int):
    dist = list(map(lambda p: list(map(lambda q: q, p)), graph))

    for r in range(vert):
        for p in range(vert):
            for q in range(vert):
                dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])

    solve(dist, vert)


def get_adjacent_cells(grid: list, cell: tuple, match: str = '') -> set:
    adjacent = set()
    x, y = cell
    max_x = len(grid[0])
    max_y = len(grid)
    adjacency = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == j == 0)]

    for dy, dx in adjacency:
        if 0 <= (x + dx) < max_x and 0 <= (y + dy) < max_y:
            if match:
                if grid[y + dy][x + dx] == match:
                    adjacent.add((x + dx, y + dy))
            else:
                adjacent.add((x + dx, y + dy))

    return adjacent
