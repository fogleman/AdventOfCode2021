import fileinput
import re

cuboids = []
for line in fileinput.input():
    x0, x1, y0, y1, z0, z1 = map(int, re.findall(r'-?\d+', line))
    cuboids.append(((x0, y0, z0), (x1+1, y1+1, z1+1), line.startswith('on')))

xs = list(sorted({e[0] for c in cuboids for e in c[:2]}))
ys = list(sorted({e[1] for c in cuboids for e in c[:2]}))
zs = list(sorted({e[2] for c in cuboids for e in c[:2]}))

def volume(i, j, k):
    x0, y0, z0 = xs[i], ys[j], zs[k]
    x1, y1, z1 = xs[i+1], ys[j+1], zs[k+1]
    dx, dy, dz = (x1 - x0), (y1 - y0), (z1 - z0)
    return dx * dy * dz

result = 0
seen = set()
for i, ((x0, y0, z0), (x1, y1, z1), on) in enumerate(cuboids):
    print(i, len(seen))
    i0, j0, k0 = xs.index(x0), ys.index(y0), zs.index(z0)
    i1, j1, k1 = xs.index(x1), ys.index(y1), zs.index(z1)
    for i in range(i0, i1):
        for j in range(j0, j1):
            for k in range(k0, k1):
                if on:
                    seen.add((i, j, k))
                else:
                    seen.discard((i, j, k))
print(len(seen))
print(sum(volume(*x) for x in seen))
