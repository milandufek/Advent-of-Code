# https://adventofcode.com/2025/day/5


def get_data(file_path) -> tuple[list[str], list[str]]:
    with open(file_path) as f:
        content = f.read()
    ranges, instructions = content.split('\n\n')
    range_lines = ranges.splitlines()
    instruction_lines = instructions.splitlines()

    return range_lines, instruction_lines


def solve_1(data: tuple[list[str], list[str]]) -> int:
    ranges, ingredients = data
    count = 0
    for i in ingredients:
        value = int(i)
        for r in ranges:
            start, end = map(int, r.split('-'))
            if start <= value <= end:
                count += 1
                break

    return count


def merge_ranges(ranges: list[tuple[int, ...]]) -> list[tuple[int, int]]:
    ranges = sorted(ranges, key=lambda r: r[0])
    merged = []
    current_start, current_end = ranges[0]
    for start, end in ranges[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end

    merged.append((current_start, current_end))

    return merged


def solve_2(data: tuple[list[str], list[str]]) -> int:
    ranges, _ = data
    ranges = [tuple(map(int, r.split('-'))) for r in ranges]
    ranges = merge_ranges(ranges)
    count = 0
    for start, end in ranges:
        count += end - start + 1

    return count


if __name__ == '__main__':
    example = get_data('inputs/05_example.in')
    data_input = get_data('inputs/05.in')
    print(f'Example #1: {solve_1(example)}')
    print(f'Score   #1: {solve_1(data_input)}')
    print(f'Example #2: {solve_2(example)}')
    print(f'Score   #2: {solve_2(data_input)}')
