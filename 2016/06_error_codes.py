from collections import Counter


# https://adventofcode.com/2016/day/5


with open('inputs/06.in') as f:
    data = f.read().splitlines()

code_1, code_2 = [], []

for col in zip(*data):
    counter = Counter(col)

    most_common_char = counter.most_common(1)[0][0]
    code_1.append(most_common_char)

    least_common_char = counter.most_common()[-1][0]
    code_2.append(least_common_char)


print('Part #1:', ''.join(code_1))
print('Part #2:', ''.join(code_2))
