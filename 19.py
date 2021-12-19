from collections import *
from itertools import *
import fileinput
import numpy as np
import re

# parse input
scanners = []
for batch in ''.join(fileinput.input()).split('\n\n'):
    x = list(map(int, re.findall(r'-?\d+', batch)[1:]))
    scanners.append(set(map(tuple, zip(x[0::3], x[1::3], x[2::3]))))

# create 24 rotation matrices
# rotations = []
# for axes in permutations([(1, 0, 0), (0, 1, 0), (0, 0, 1)]):
#     for signs in combinations_with_replacement((1, -1), 3):
#         rotations.append(np.array([np.array(a) * s
#             for a, s in zip(axes, signs)]))

rotations = [np.array(x).reshape(3, 3) for x in [
    ( 1, 0, 0, 0, 1, 0, 0, 0, 1),
    ( 1, 0, 0, 0, 0, 1, 0,-1, 0),
    ( 1, 0, 0, 0, 0,-1, 0, 1, 0),
    ( 1, 0, 0, 0,-1, 0, 0, 0,-1),
    ( 0, 1, 0, 1, 0, 0, 0, 0,-1),
    ( 0, 1, 0, 0, 0, 1, 1, 0, 0),
    ( 0, 1, 0, 0, 0,-1,-1, 0, 0),
    ( 0, 1, 0,-1, 0, 0, 0, 0, 1),
    ( 0, 0, 1, 1, 0, 0, 0, 1, 0),
    ( 0, 0, 1, 0, 1, 0,-1, 0, 0),
    ( 0, 0, 1, 0,-1, 0, 1, 0, 0),
    ( 0, 0, 1,-1, 0, 0, 0,-1, 0),
    ( 0, 0,-1, 1, 0, 0, 0,-1, 0),
    ( 0, 0,-1, 0, 1, 0, 1, 0, 0),
    ( 0, 0,-1, 0,-1, 0,-1, 0, 0),
    ( 0, 0,-1,-1, 0, 0, 0, 1, 0),
    ( 0,-1, 0, 1, 0, 0, 0, 0, 1),
    ( 0,-1, 0, 0, 0, 1,-1, 0, 0),
    ( 0,-1, 0, 0, 0,-1, 1, 0, 0),
    ( 0,-1, 0,-1, 0, 0, 0, 0,-1),
    (-1, 0, 0, 0, 1, 0, 0, 0,-1),
    (-1, 0, 0, 0, 0, 1, 0, 1, 0),
    (-1, 0, 0, 0, 0,-1, 0,-1, 0),
    (-1, 0, 0, 0,-1, 0, 0, 0, 1),
]]

def translations(a, b):
    counts = defaultdict(int)
    for (x0, y0, z0) in a:
        for (x1, y1, z1) in b:
            counts[(x0 - x1, y0 - y1, z0 - z1)] += 1
    result = []
    hi = max(counts.values())
    for k, v in counts.items():
        if v >= hi and v >= 12:
            result.append(k)
    return result

def rotate(m, points):
    return {tuple(m @ p) for p in points}

def translate(t, points):
    dx, dy, dz = t
    return {(x + dx, y + dy, z + dz) for x, y, z in points}

def match(a, b):
    for m in rotations:
        c = rotate(m, b)
        for t in translations(a, c):
            d = translate(t, c)
            d = set(map(tuple, d))
            e = a & d
            if len(e) >= 12:
                p = list(translate(t, rotate(m, [(0, 0, 0)])))[0]
                return d, p
    return None, None

while True:
    done = True
    seen = set()
    for i, a in enumerate(scanners):
        for j, b in enumerate(scanners):
            if i >= j:
                continue
            key = (i, j, len(b))
            if key in seen:
                continue
            seen.add(key)
            c, p = match(a, b)
            if c is None:
                continue
            if c - a:
                done = False
                a |= c
                print(i, j, len(a))
    if done:
        break

print(len(scanners[0]))

positions = []
for i, s in enumerate(scanners):
    _, p = match(scanners[0], s)
    positions.append(p)

def manhattan(a, b):
    x0, y0, z0 = a
    x1, y1, z1 = b
    return abs(x1 - x0) + abs(y1 - y0) + abs(z1 - z0)

print(max(manhattan(a, b) for a in positions for b in positions))
