import re
from my_utils import get_data


def check_nice_1(s: str) -> int:
    first = 0
    for i in 'aeiou':
        first += s.count(i)

    twice = False
    prev = ' '
    for j in s + ' ':
        if j == prev:
            twice = True
            break
        prev = j

    third = True
    cannot = ['ab', 'cd', 'pq', 'xy']
    for k in cannot:
        if k in s:
            third = False
            break

    if first >= 3 and twice and third:
        return 1

    return 0


re_repeat = re.compile(r'(.).\1')
re_dup = re.compile(r'(..).*\1')

def check_nice_2(s: str) -> int:
    if re_repeat.search(s) is None:
        return 0
    return int(re_dup.search(s) is not None)


count_1 = 0
count_2 = 0
data = get_data('inputs/05.in')

for line in data:
    count_1 += check_nice_1(line)
    count_2 += check_nice_2(line)

print(f'Count #1: {count_1}')
print(f'Count #2: {count_2}')
