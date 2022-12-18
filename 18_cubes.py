from utils import get_data


# https://adventofcode.com/2022/day/18


def approx_surface(data: list) -> None:
    cubes = []
    neighbor_pairs = 0
    deltas = [(1, 0, 0), (-1, 0, 0),
              (0, 1, 0), (0, -1, 0),
              (0, 0, 1), (0, 0, -1)]

    for i in data:
        x, y, z = map(int, i.split(','))
        cubes.append((x, y, z))

        for dx, dy, dz in deltas:
            neighbor_cube = (x + dx, y + dy, z + dz)

            if neighbor_cube in cubes:
                neighbor_pairs += 1

    print(f'Surface #1: {6 * len(cubes) - 2 * neighbor_pairs}')


if __name__ == '__main__':
    # data = get_data('inputs/18_example.in')
    data = get_data('inputs/18.in')
    approx_surface(data)
