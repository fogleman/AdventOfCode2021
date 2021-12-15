import fileinput
import heapq

grid = [list(map(int, x.strip())) for x in fileinput.input()]
cells = dict(((x, y), v) for y, r in enumerate(grid) for x, v in enumerate(r))

def large(cells):
    result = {}
    w, h = max(cells)
    w, h = w + 1, h + 1
    for y in range(h * 5):
        for x in range(w * 5):
            v = (cells[(x % w, y % h)] + x // w + y // h - 1) % 9 + 1
            result[(x, y)] = v
    return result

def heuristic(p, t, v):
    dx = abs(p[0] - t[0])
    dy = abs(p[1] - t[1])
    return v + (dx + dy) ** 1.001

def shortest_path(cells, source, target):
    seen, queue = set(), [(heuristic(source, target, 0), 0, source)]
    while queue:
        _, d, p = heapq.heappop(queue)
        if p == target:
            return d
        seen.add(p)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            q = (p[0] + dx, p[1] + dy)
            if q in cells and q not in seen:
                heapq.heappush(queue,
                    (heuristic(q, target, d + cells[q]), d + cells[q], q))

print(shortest_path(cells, (0, 0), max(cells)))
cells = large(cells)
print(shortest_path(cells, (0, 0), max(cells)))
