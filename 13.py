import fileinput
import re

data = ''.join(fileinput.input())
dots = {(int(x), int(y)) for x, y in re.findall(r'(\d+),(\d+)', data)}
folds = [(a, int(n)) for a, n in re.findall(r'([xy])=(\d+)', data)]

def fold(dots, a, p):
    f = lambda x: x if x < p else p - (x - p)
    return {(f(x), y) if a == 'x' else (x, f(y)) for x, y in dots}

for i, (a, p) in enumerate(folds):
    dots = fold(dots, a, p)
    if i == 0:
        print(len(dots))

for y in range(max(d[1] for d in dots) + 1):
    for x in range(max(d[0] for d in dots) + 1):
        print('*' if (x, y) in dots else ' ', end='')
    print()
