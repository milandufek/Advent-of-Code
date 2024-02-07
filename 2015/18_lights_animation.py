def solve(input_file: list, part: int):
    corners = {(0,0), (0,99), (99,0), (99,99)} if part == 2 else set()

    with open(input_file) as f:
        lights = {(x,y) for y, line in enumerate(f)
                  for x, char in enumerate(line.strip())
                  if char == '#'}
        lights = corners | lights

    neighbors = lambda x, y: sum((_x, _y) in lights for _x in (x - 1, x, x + 1)
                                 for _y in (y - 1, y, y + 1)
                                 if (_x, _y) != (x, y))

    for _ in range(100):
        lights = {(x, y) for x in range(100) for y in range(100)
                  if (x, y) in lights and 2 <= neighbors(x, y) <= 3
                  or (x, y) not in lights and neighbors(x, y) == 3}
        lights = corners | lights

    print(len(lights))


if __name__ == '__main__':
    solve('inputs/18.in', part=1)
    solve('inputs/18.in', part=2)
