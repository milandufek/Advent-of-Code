INPUT = '1113222113'


def convert(s: str) -> str:
    result = ''
    count = 1
    prev = ' '

    for i, letter in enumerate(s + ' '):
        if letter == prev:
            count += 1
            prev = letter
            continue

        if i != 0:
            result += str(count)
            result += prev

        count = 1
        prev = letter

    return result


def repeat(n: int, s: str = INPUT) -> int:
    r = ''
    for _ in range(n):
        if not r:
            r = convert(s)
            continue

        r = convert(r)

    return len(r)


print('Result #1:', repeat(40))
print('Result #2:', repeat(50))
