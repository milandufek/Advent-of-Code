import re


signature = {
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

nums = re.compile(r'\d+')
name = re.compile(r'(?<=\s)[a-z]+')

for line in lines:
    vals, names = list(map(int, nums.findall(line))), name.findall(line)
    sue_number = vals.pop(0)

    if all(x == y for x, y in zip(map(signature.get, names), vals)):
        print(list(zip(map(signature.get, names), vals)))
        print(sue_number)
