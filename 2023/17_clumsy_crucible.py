import heapq
from my_utils import get_data


# https://adventofcode.com/2023/day/17


def solve_1(lines: list[str]) -> int:
    heat_map: list[list[int]] = [list(map(int, list(line.strip()))) for line in lines]
    rows = len(heat_map)
    cols = len(heat_map[0])
    end = (rows - 1, cols - 1)
    pq = [(0, 0, 0, 0, 0, 0)]  # heat, r, c, dir_r, dir_c, steps_in_direction
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while pq:
        heat, r, c, dr, dc, in_dir = heapq.heappop(pq)

        if (r, c) == end:
            return heat

        if (r, c, dr, dc, in_dir) in visited:
            continue

        visited.add((r, c, dr, dc, in_dir))

        if in_dir < 3 and (dr, dc) != (0, 0):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                heapq.heappush(pq, (heat + heat_map[nr][nc], nr, nc, dr, dc, in_dir + 1))

        for ndr, ndc in directions:
            if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                nr, nc = r + ndr, c + ndc
                if 0 <= nr < rows and 0 <= nc < cols:
                    heapq.heappush(pq, (heat + heat_map[nr][nc], nr, nc, ndr, ndc, 1))

    return -1


def solve_2(lines: list[str]) -> int:
    heat_map: list[list[int]] = [list(map(int, list(line.strip()))) for line in lines]
    rows = len(heat_map)
    cols = len(heat_map[0])
    end = (rows - 1, cols - 1)
    pq = [(0, 0, 0, 0, 0, 0)]  # heat, r, c, dir_r, dir_c, steps_in_direction
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while pq:
        heat, r, c, dr, dc, in_dir = heapq.heappop(pq)

        if (r, c) == end and in_dir >= 4:
            return heat

        if (r, c, dr, dc, in_dir) in visited:
            continue

        visited.add((r, c, dr, dc, in_dir))

        if in_dir < 10 and (dr, dc) != (0, 0):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                heapq.heappush(pq, (heat + heat_map[nr][nc], nr, nc, dr, dc, in_dir + 1))

        if in_dir >= 4 or (dr, dc) == (0, 0):
            for ndr, ndc in directions:
                if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                    nr, nc = r + ndr, c + ndc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        heapq.heappush(pq, (heat + heat_map[nr][nc], nr, nc, ndr, ndc, 1))

    return -1


if __name__ == '__main__':
    example = get_data('inputs/17_example.in')
    data_input = get_data('inputs/17.in')
    print(f'Example #1: {solve_1(example)}')
    print(f'Score #1: {solve_1(data_input)}')
    print(f'Example #2: {solve_2(example)}')
    print(f'Score #2: {solve_2(data_input)}')
