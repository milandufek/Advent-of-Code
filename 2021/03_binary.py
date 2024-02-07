with open('inputs/03.in') as f:
    lines = list(map(list, f.readlines()))


z = list(map(list, zip(*lines)))
i = (''.join(max(k, key=k.count) for k in z))
j = (''.join(min(k, key=k.count) for k in z))

print('#1:', int(i, 2) * int(j, 2))
