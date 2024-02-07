with open('inputs/01.in') as f:
    n = list(map(int, f.read().strip()))

print('#1:', sum(a for a, b in zip(n, n[1:] + [n[0]]) if a == b))

half = len(n) // 2
print('#2:', sum(a + b for a, b in zip(n[half:], n[:half]) if a == b))
