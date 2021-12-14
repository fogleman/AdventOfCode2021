from collections import defaultdict
import fileinput

G = defaultdict(set)
for line in fileinput.input():
    a, b = line.strip().split('-')
    G[a].add(b)
    G[b].add(a)

def search(G, path, twice):
    if path[-1] == 'end':
        yield list(path)
        return
    for p in G[path[-1]]:
        small = p == p.lower()
        if p == 'start' or (twice and small and p in path):
            continue
        path.append(p)
        yield from search(G, path, twice or (small and path.count(p) > 1))
        path.pop()

print(len(list(search(G, ['start'], True))))
print(len(list(search(G, ['start'], False))))
