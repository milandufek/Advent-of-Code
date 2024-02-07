from utils import get_data


directions = get_data('inputs/03.in')
grid = set()
x = y = 0

for d in directions[0]:
    grid.add((x, y))

    match d:
        case '>':
            x += 1
        case '<':
            x -= 1
        case '^':
            y += 1
        case 'v':
            y -= 1


grid_s = set()
grid_r = set()
xs = xr = ys = yr = 0

for i, d in enumerate(directions[0]):
    grid_s.add((xs, ys))
    grid_r.add((xr, yr))

    if i % 2 == 0:
        match d:
            case '>':
                xs += 1
            case '<':
                xs -= 1
            case '^':
                ys += 1
            case 'v':
                ys -= 1
    else:
        match d:
            case '>':
                xr += 1
            case '<':
                xr -= 1
            case '^':
                yr += 1
            case 'v':
                yr -= 1


print(f'Visited #1: {len(grid)}')
print(f'Visited #2: {len(grid_s | grid_r)}')
