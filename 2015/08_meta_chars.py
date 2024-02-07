from my_utils import get_data


chars = mem = diff = 0

for line in get_data('inputs/08.in'):
    line = line.strip()
    chars += len(line)
    mem += len(eval(line))
    diff += line.count('\\') + line.count('"') + 2

print(chars - mem, diff)
