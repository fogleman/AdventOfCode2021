from collections import defaultdict
import fileinput
import re

lines = [tuple(map(int, re.findall(r'\d+', line)))
    for line in fileinput.input()]

def run(lines, diagonal):
    grid = defaultdict(int)
    step = lambda a: (a > 0) - (a < 0)
    for x0, y0, x1, y1 in lines:
        dx, dy = step(x1 - x0), step(y1 - y0)
        if dx and dy and not diagonal:
            continue
        x, y = x0, y0
        while True:
            grid[(x, y)] += 1
            if (x, y) == (x1, y1):
                break
            x, y = x + dx, y + dy
    return sum(x > 1 for x in grid.values())

print(run(lines, 0))
print(run(lines, 1))
