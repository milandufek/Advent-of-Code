with open('inputs/01.in') as f:
    lines = list(map(int, f.readlines()))

print('#1:', sum(a < b for a, b in zip(lines, lines[1:])))

trinity = [sum(x) for x in zip(lines, lines[1:], lines[2:])]
print('#2:', sum(a < b for a, b in zip(trinity, trinity[1:])))
