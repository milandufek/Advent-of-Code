# https://adventofcode.com/2015/day/11


def has_sequence(password: str) -> bool:
    nums = list(map(ord, password))

    def check_seq(a, b, c):
        return a == b - 1 and b == c - 1

    return any(map(check_seq, nums, nums[1:], nums[2:]))


def has_invalid_chars(password: str) -> bool:
    return any(c in password for c in 'iol')


def has_two_pairs(password: str) -> bool:
    nums = list(map(ord, password))
    pairs = set()

    for nums, next_nums in zip(nums, nums[1:]):
        if nums == next_nums:
            pairs.add(nums)

    return len(pairs) >= 2


def is_valid(password: str) -> bool:
    return (
        not has_invalid_chars(password)
        and has_sequence(password)
        and has_two_pairs(password)
    )


def get_next_char(c: str) -> str:
    if c == 'z':
        return 'a'

    return chr(ord(c) + 1)


def increment_password(password: str) -> str:
    next_char = get_next_char(password[-1])

    if next_char == 'a':
        return increment_password(password[:-1]) + next_char

    next_char = password[:-1] + next_char

    return next_char


def solve(password: str) -> str:
    password = increment_password(password)

    while not is_valid(password):
        password = increment_password(password)

    return password


def test_char_increase():
    assert get_next_char('a') == 'b'
    assert get_next_char('z') == 'a'


def test_has_sequence():
    assert has_sequence('xxxabcxxx')
    assert has_sequence('xyzde')
    assert not has_sequence('zxy')
    assert not has_sequence('abdabdabd')
    assert not has_sequence('aaaaaaaaa')


def test_has_invalid_chars():
    assert has_invalid_chars('iol')
    assert not has_invalid_chars('abc')
    assert not has_invalid_chars('def')


def test_has_two_pairs():
    assert has_two_pairs('aabb')
    assert has_two_pairs('abccdd')
    assert has_two_pairs('aaccdd')
    assert not has_two_pairs('abcde')
    assert not has_two_pairs('abcdee')
    assert not has_two_pairs('abccde')
    assert not has_two_pairs('aabc')


def test_is_valid():
    assert is_valid('abcdffaa')
    assert is_valid('ghjaabcc')
    assert not is_valid('abbceffg')
    assert not is_valid('abbcegjk')
    assert not is_valid('abcdeggg')


def test_solve():
    assert solve('abcdefgh') == 'abcdffaa'
    assert solve('ghijklmn') == 'ghjaabcc'
    assert solve('vzbxxyzz') == 'vzcaabcc'


if __name__ == '__main__':
    _input = 'vzbxkghb'
    first_next = solve(_input)
    print(f'Score #1: {first_next}')
    second_next = solve(first_next)
    print(f'Score #2: {second_next}')
