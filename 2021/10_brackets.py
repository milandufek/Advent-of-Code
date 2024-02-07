POINTS_1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
POINTS_2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

# with open('inputs/10_example.in') as f:
with open('inputs/10.in') as f:
    lines = f.readlines()

brackets = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>',
}

score = 0

for line in lines:
    stack = []
    for char in line.strip():
        if char in brackets:
            stack.append(brackets[char])
        elif char == stack[-1]:
            stack.pop()
        else:
            score += POINTS_1[char]
            break

print('#1:', score)

#
# part 2
#

score = []

for line in lines:
    stack = []
    for char in line.strip():
        if char in brackets:
            stack.append(brackets[char])
        elif char == stack[-1]:
            stack.pop()
        else:
            break
    else:
        x = 0
        for i in reversed(stack):
            x *= 5
            x += POINTS_2[i]

        score.append(x)

score.sort()
print('#2:', score[len(score) // 2])
