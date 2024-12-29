# https://adventofcode.com/2019/day/2


with open('inputs/01.txt') as f:
    nums = list(map(int, f.readlines()))

fuel = lambda x: x // 3 - 2

print('#1:', sum(map(fuel, nums)))


def total_fuel(x):
    y = fuel(x)
    return y + total_fuel(y) if y >= 0 else 0

# print('#2:', sum(total_fuel(x) for x in nums))
print('#2:', sum(map(total_fuel, nums)))
