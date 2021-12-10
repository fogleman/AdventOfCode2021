import fileinput

grid = [list(map(int, line.strip())) for line in fileinput.input()]
w, h = len(grid[0]), len(grid)

def neighbors(x, y):
    result = []
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nx, ny = x + dx, y + dy
        if nx >= 0 and ny >= 0 and nx < w and ny < h:
            result.append(grid[ny][nx])
    return result

print(sum(grid[y][x] + 1 if all(grid[y][x] < n for n in neighbors(x, y)) else 0
    for y in range(h) for x in range(w)))

def fill(x, y, v):
    if grid[y][x] == 9:
        return 0
    if basins[y][x] >= 0:
        return 0
    basins[y][x] = v
    result = 1
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nx, ny = x + dx, y + dy
        if nx >= 0 and ny >= 0 and nx < w and ny < h:
            result += fill(nx, ny, v)
    return result

basins = [[-1] * w for _ in range(h)]
basin = 0
sizes = []
for y in range(h):
    for x in range(w):
        size = fill(x, y, basin)
        if size:
            sizes.append(size)
            basin += 1
sizes.sort()
print(sizes[-1] * sizes[-2] * sizes[-3])
