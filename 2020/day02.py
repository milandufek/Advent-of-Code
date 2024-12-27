x = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc',
]

with open('inputs/02.txt') as f:
    x = f.readlines()

valid = 0
valid_2 = 0

for line in x:
    _range, letter, password = line.split()
    _min, _max = map(int, _range.split('-'))
    letter = letter[0]
    count = password.count(letter)

    if _min <= count <= _max:
        valid += 1

    password = ' ' + password

    if (password[_min] == letter) != (password[_max] == letter):
        valid_2 += 1


print(f'#1: {valid}')
print(f'#2: {valid_2}')
