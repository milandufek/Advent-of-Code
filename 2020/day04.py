from typing import Generator


# https://adventofcode.com/2020/day/4


def get_data(file_path: str) -> Generator[str, None, None]:
    with open(file_path) as f:
        return (line.replace('\n', ' ').strip() for line in f.read().split('\n\n'))


def solve_1(passports: Generator[str, None, None]) -> int:
    mandatory_fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
    return sum(all(field in passport for field in mandatory_fields) for passport in passports)


def validate_passport(passport: str) -> bool:
    mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    fields = {field.split(':')[0].strip(): field.split(':')[1].strip() for field in passport.split()}
    if any(mandatory not in fields.keys() for mandatory in mandatory_fields):
        return False
    if not 1920 <= int(fields['byr']) <= 2002:
        return False
    if not 2010 <= int(fields['iyr']) <= 2020:
        return False
    if not 2020 <= int(fields['eyr']) <= 2030:
        return False
    if fields['hgt']:
        value = fields['hgt']
        if not (value.endswith('cm') or value.endswith('in')):
            return False
        if value.endswith('cm') and not 150 <= int(value[:-2]) <= 193:
            return False
        elif value.endswith('in') and not 59 <= int(value[:-2]) <= 76:
            return False
    if fields['hcl']:
        value = fields['hcl']
        if not value.startswith('#') or len(value) != 7:
            return False
        if any(c not in '0123456789abcdef' for c in value[1:]):
            return False
    if fields['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if fields['pid']:
        value = fields['pid']
        if not value.isnumeric() or len(value) != 9:
            return False

    return True

def solve_2(passports: Generator[str, None, None]) -> int:
    return sum(validate_passport(passport) for passport in passports)


if __name__ == '__main__':
    data_input = get_data('inputs/04.txt')
    print(f'#1: {solve_1(data_input)}')
    data_input = get_data('inputs/04.txt')
    print(f'#2: {solve_2(data_input)}')
