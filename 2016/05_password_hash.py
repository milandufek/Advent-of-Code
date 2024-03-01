from hashlib import md5


# https://adventofcode.com/2016/day/5


def solve_1(_hash: str) -> str:
    password = []
    i = 0
    while len(password) < 8:
        h = md5(f'{_hash}{i}'.encode()).hexdigest()

        if h.startswith('00000'):
            password.append(h[5])

        i += 1

    return ''.join(password)


def solve_2(_hash: str) -> str:
    password = ['_'] * 8
    i = 0
    while '_' in password:
        h = md5(f'{_hash}{i}'.encode()).hexdigest()
        i += 1

        if h.startswith('00000'):
            if not h[5].isdigit():
                continue

            index = int(h[5])

            if 0 <= index < 8 and password[index] == '_':
                password[index] = h[6]

    return ''.join(password)


if __name__ == '__main__':
    _hash = 'uqwqemis'
    print(f'Part 1: {solve_1(_hash)}')
    print(f'Part 2: {solve_2(_hash)}')
