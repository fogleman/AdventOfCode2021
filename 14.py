from collections import *
import fileinput
import re

data = ''.join(fileinput.input())
polymer = data.split()[0]
rules = dict(re.findall(r'(\w\w) -> (\w)', data))

def step(counts, rules):
    result = defaultdict(int)
    for (a, b), n in counts.items():
        c = rules[a + b]
        result[a + c] += n
        result[c + b] += n
    return result

def score(counts):
    result = defaultdict(int)
    for (a, b), n in counts.items():
        result[a] += n
        result[b] += n
    a = result.values()
    return (max(a) - min(a)) // 2 + 1

counts = Counter(a + b for a, b in zip(polymer, polymer[1:]))
for i in range(40):
    counts = step(counts, rules)
    if i in (9, 39):
        print(score(counts))
