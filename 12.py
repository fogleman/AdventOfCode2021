from collections import defaultdict, Counter
import fileinput

G = defaultdict(set)
for line in fileinput.input():
    a, b = line.strip().split('-')
    G[a].add(b)
    G[b].add(a)

def search(G, path, one):
    pos = path[-1]
    if pos == 'end':
        yield list(path)
        return
    for p in G[pos]:
        if one:
            if p == p.lower() and p in path:
                continue
        else:
            c = Counter(path)
            n = [v for k, v in c.items() if k == k.lower()]
            if c['start'] > 1 or any(x > 2 for x in n) or sum(x > 1 for x in n) > 1:
                continue
        path.append(p)
        yield from search(G, path, one)
        path.pop()

print(len(list(search(G, ['start'], 1))))
print(len(list(search(G, ['start'], 0))))
