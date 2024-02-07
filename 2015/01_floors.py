with open('inputs/01.in') as f:
    doors = f.read()

open = doors.count('(')
close = doors.count(')')

print(f'Result #1: {open - close}')

current = 0
for i, s in enumerate(doors, start=1):
    current += 1 if s == '(' else -1
    if current == -1:
        break

print(f'Result #2: {i}')
