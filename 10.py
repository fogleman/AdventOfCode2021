import fileinput

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

points2 = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

def process(line):
    stack = []
    for c in line:
        if c in '([{<':
            stack.append(c)
        else:
            d = stack.pop()
            if abs(ord(c) - ord(d)) > 2:
                return points[c]
    return 0

def process2(line):
    stack = []
    for c in line:
        if c in '([{<':
            stack.append(c)
        else:
            d = stack.pop()
            if abs(ord(c) - ord(d)) > 2:
                return None
    s = 0
    while stack:
        c = stack.pop()
        s = s * 5 + points2[c]
    return s

lines = []
for line in fileinput.input():
    lines.append(line.strip())

print(sum(process(line) for line in lines))

scores = list(filter(None, [process2(line) for line in lines]))
scores.sort()
print(scores[len(scores) // 2])
