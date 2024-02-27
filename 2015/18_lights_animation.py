def sum_of_neighbors(lights: set[tuple[int, int]], x: int, y: int) -> int:
    return sum(
        (nx, ny) in lights
        for nx in (x - 1, x, x + 1)
        for ny in (y - 1, y, y + 1)
        if (nx, ny) != (x, y)
    )


def solve(input_file: list, part: int) -> None:
    corners = {(0,0), (0,99), (99,0), (99,99)} if part == 2 else set()

    with open(input_file) as f:
        lights = {
            (x,y) for y, line in enumerate(f)
            for x, char in enumerate(line.strip())
            if char == '#'
        }
        lights = corners | lights

    for _ in range(100):
        lights = {
            (x, y) for x in range(100) for y in range(100)
            if (x, y) in lights and 2 <= sum_of_neighbors(lights, x, y) <= 3
            or (x, y) not in lights and sum_of_neighbors(lights, x, y) == 3
        }
        lights = corners | lights

    print(len(lights))


if __name__ == '__main__':
    solve('inputs/18.in', part=1)
    solve('inputs/18.in', part=2)
