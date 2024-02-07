from itertools import permutations


with open('inputs/08.in') as f:
    lines = f.readlines()

printable = 0
for line in lines:
    _, out = line.split('|')
    for digit in out.split():
        if len(digit) in (2, 3, 4, 7):
            printable += 1

print('#1:', printable)


count = 0
for k in lines:
    _in, _out = k.split('|')
    do = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
    req = set(do)

    for x in permutations('abcdefg'):
        m = {k: v for k, v in zip(x, 'abcdefg')}
        r = {''.join(sorted(map(m.get, x))) for x in _in.split()}

        if r == req:
            _out = [''.join(sorted(map(m.get, x))) for x in _out.split()]
            _out = ''.join(str(do.index(x)) for x in _out)
            count += int(_out)

print('#2:', count)
