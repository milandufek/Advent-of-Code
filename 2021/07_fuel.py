# positions = [16,1,2,0,4,2,7,1,2,14]
with open('inputs/07.in') as f:
    positions = list(map(int, f.read().strip().split(',')))

best = 999999999
for i in range(min(positions), max(positions)):
    fuel = sum([abs(p - i) for p in positions])
    best = min(fuel, best)

print('#1:', best)

cost = lambda x: x * (x + 1) // 2
best = 999999999
for i in range(min(positions), max(positions)):
    fuel = sum([cost(abs(p - i)) for p in positions])
    best = min(fuel, best)

print('#2:', best)
