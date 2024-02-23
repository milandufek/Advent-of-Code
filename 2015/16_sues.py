import re


_signature = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

with open('inputs/16.in') as f:
    lines = f.readlines()

re_nums = re.compile(r'\d+')
re_name = re.compile(r'(?<=\s)[a-z]+')


def solve_1() -> None:
    for line in lines:
        vals, names = list(map(int, re_nums.findall(line))), re_name.findall(line)
        sue_number = vals.pop(0)

        if all(x == y for x, y in zip(map(_signature.get, names), vals)):
            print(f'#1: {sue_number}')


def indicate(name: str, x: int, y: int) -> bool:
    if name in ('tree', 'cats'):
        return x > y

    if name in ('pomeranians', 'goldfish'):
        return x < y

    return x == y


def solve_2() -> None:
    for line in lines:
        vals, names = list(map(int, re_nums.findall(line))), re_name.findall(line)
        sue_number = vals.pop(0)

        if all(indicate(name, val, _signature[name]) for name, val in zip(names, vals)):
            print(f'#2: {sue_number}')


if __name__ == '__main__':
    solve_1()
    solve_2()
