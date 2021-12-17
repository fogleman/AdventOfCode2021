import fileinput
import re

bounds = tuple(map(int, re.findall(r'[-\d]+', ''.join(fileinput.input()))))

def run(v, bounds):
    x = y = hi = 0
    vx, vy = v
    x0, x1, y0, y1 = bounds
    while True:
        x += vx
        y += vy
        hi = max(hi, y)
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        vy -= 1
        if x0 <= x <= x1 and y0 <= y <= y1:
            return hi
        if (y < y0 and vy < 0) or (x < x0 and vx <= 0) or (x > x1 and vx >= 0):
            return None

n = hi = count = 0
while True:
    n += 1
    for vy in range(-n, n + 1):
        for vx in range(-n, n + 1) if vy in [-n, n] else [-n, n]:
            y = run((vx, vy), bounds)
            if y is None:
                continue
            count += 1
            hi = max(hi, y)
            print(hi, count, (vx, vy))
