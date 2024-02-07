from utils import get_data


# https://adventofcode.com/2023/day/5


def solve_1(_input_file: str) -> int:
    with open(_input_file) as f:
        data = f.read().split('\n\n')

    seeds, *blocks = data
    seeds = list(map(int, seeds.split()[1:]))

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))

        new = []
        for seed in seeds:
            for dest, source, step in ranges:
                if source <= seed < source + step:
                    new.append(seed - source + dest)
                    break
            else:
                new.append(seed)

        seeds = new

    return min(new)


if __name__ == '__main__':
    example = 'inputs/05_example.in'
    data = 'inputs/05.in'
    print(f'Example #1: {solve_1(example)}')
    print(f'Score #1: {solve_1(data)}')
    #print(f'Example #2: {solve_2(example)}')
    #print(f'Score #2: {solve_2(data)}')
