import fileinput

lines = list(fileinput.input())
rules = lines[0]
cells = {(x, y) for y, line in enumerate(lines[2:])
    for x, c in enumerate(line) if c == '#'}

def include(rules, cells, x, y, flip):
    index = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            index = index << 1 | ((x + dx, y + dy) in cells) ^ flip
    return (rules[index] == '.') ^ flip

def step(rules, cells, flip):
    x0, y0 = min(x[0] for x in cells) - 1, min(x[1] for x in cells) - 1
    x1, y1 = max(x[0] for x in cells) + 2, max(x[1] for x in cells) + 2
    return {(x, y) for y in range(y0, y1) for x in range(x0, x1)
        if include(rules, cells, x, y, flip)}

counts = []
for i in range(50):
    cells = step(rules, cells, i % 2)
    counts.append(len(cells))

print(counts[1])
print(counts[-1])
