with open('inputs/03.in') as f:
    lines = list(map(list, f.readlines()))


z = list(map(list, zip(*lines)))
i = (''.join(max(k, key=k.count) for k in z))
j = (''.join(min(k, key=k.count) for k in z))

print('#1:', int(i, 2) * int(j, 2))


def cut(items, criteria, index = 0):
    v = [item[index] for item in items]
    q = criteria(v, key = lambda x: (v.count(x), x))
    items = [item for item in items if item[index] == q]

    if len(items) == 1:
        return items[0]

    return cut(items, criteria, index + 1)

ox = int(''.join(cut(lines, max)), 2)
co = int(''.join(cut(lines, min)), 2)

print('#2:', ox * co)
