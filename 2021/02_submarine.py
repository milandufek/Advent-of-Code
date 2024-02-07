with open('inputs/02.in') as f:
    lines = f.readlines()


depth = horizontal = 0
for line in lines:
    action, i = line.split()
    i = int(i)
    match action:
        case 'forward':
            horizontal += i
        case 'up':
            depth -= i
        case 'down':
            depth += i

print('#1:', depth * horizontal)


aim = depth = horizontal = 0
for line in lines:
    action, i = line.split()
    i = int(i)
    match action:
        case 'forward':
            horizontal += i
            depth += aim * i
        case 'up':
            aim -= i
        case 'down':
            aim += i

print('#2:', depth * horizontal)
