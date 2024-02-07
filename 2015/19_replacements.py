import re
from collections import defaultdict


transitions = defaultdict(list)


with open('inputs/19.in') as f:
    rules, text = f.read().split('\n\n')

lines = rules.split('\n')

for line in lines:
    a, b = line.split(' => ')
    transitions[a].append(b)

units = re.compile(r'[A-Z][a-z]*')
endpoints = set()
tokens = units.findall(text)

for i, token in enumerate(tokens):
    for terminal in transitions[token]:
        l = tokens.copy()
        l[i] = terminal
        endpoints.add(''.join(l))

print(len(endpoints))
