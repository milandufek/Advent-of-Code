from my_utils import get_data


INPUT = get_data('inputs/02.in')

total_1 = 0
for i in INPUT:
    a, b, c = map(int, i.split('x'))
    o = 2 * a * b + 2 * b * c + 2 * a * c
    sorted_sides = sorted([a, b, c])
    extra = sorted_sides[0] * sorted_sides[1]
    total_1 += o + extra


total_2 = 0
for i in INPUT:
    a, b, c = sorted(map(int, i.split('x')))
    total_2 += a + a + b + b + (a * b * c)


print(f'#1: {total_1}')
print(f'#2: {total_2}')
