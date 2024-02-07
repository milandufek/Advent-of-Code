from itertools import cycle

with open('inputs/01.in') as f:
    nums = list(map(int, f.readlines()))

print('#1:', sum(nums))

x = 0
results = {x: 1}

for i in cycle(nums):
    x += i

    if results.get(x):
        print('#2:', x)
        break

    results[x] = 1
