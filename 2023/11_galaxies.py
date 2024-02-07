from utils import get_data


# https://adventofcode.com/2023/day/11


def solve(data: list, scale_factor: int = 2) -> int:
    empty_rows = [r for r, row in enumerate(data)
                  if all(ch == '.' for ch in row)]
    empty_cols = [c for c, col in enumerate(zip(*data))
                  if all(ch == '.' for ch in col)]

    points = [(r, c) for r, row in enumerate(data)
              for c, ch in enumerate(row)
              if ch == '#']

    total = 0

    for i, (r1, c1) in enumerate(points):
        for (r2, c2) in points[:i]:
            for r in range(min(r1, r2), max(r1, r2)):
                total += scale_factor if r in empty_rows else 1
            for c in range(min(c1, c2), max(c1, c2)):
                total += scale_factor if c in empty_cols else 1

    return total


if __name__ == '__main__':
    example = get_data('inputs/11_example.in')
    data = get_data('inputs/11.in')
    print(f'Example #1: {solve(example)}')
    print(f'Score #1: {solve(data)}')
    print(f'Example #2: {solve(example, 100)}')
    print(f'Score #2: {solve(data, 1_000_000)}')
