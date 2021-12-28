from collections import defaultdict
import fileinput
import heapq
import re

rooms = ['A1','B1','C1','D1','A2','B2','C2','D2','A3','B3','C3','D3','A4','B4','C4','D4']
state = tuple(sorted(zip(rooms, re.findall(r'[ABCD]', ''.join(fileinput.input())))))
solved = tuple(sorted(zip(rooms, 'ABCD' * (len(state) // 4))))

def generate_lookup_table(n):
    table = [
        ('A', 'H1', 3, {'H2'}),
        ('A', 'H2', 2, set()),
        ('A', 'H3', 2, set()),
        ('A', 'H4', 4, {'H3'}),
        ('A', 'H5', 6, {'H3','H4'}),
        ('A', 'H6', 8, {'H3','H4','H5'}),
        ('A', 'H7', 9, {'H3','H4','H5','H6'}),
        ('B', 'H1', 5, {'H2','H3'}),
        ('B', 'H2', 4, {'H3'}),
        ('B', 'H3', 2, set()),
        ('B', 'H4', 2, set()),
        ('B', 'H5', 4, {'H4'}),
        ('B', 'H6', 6, {'H4','H5'}),
        ('B', 'H7', 7, {'H4','H5','H6'}),
        ('C', 'H1', 7, {'H2','H3','H4'}),
        ('C', 'H2', 6, {'H3','H4'}),
        ('C', 'H3', 4, {'H4'}),
        ('C', 'H4', 2, set()),
        ('C', 'H5', 2, set()),
        ('C', 'H6', 4, {'H5'}),
        ('C', 'H7', 5, {'H5','H6'}),
        ('D', 'H1', 9, {'H2','H3','H4','H5'}),
        ('D', 'H2', 8, {'H3','H4','H5'}),
        ('D', 'H3', 6, {'H4','H5'}),
        ('D', 'H4', 4, {'H5'}),
        ('D', 'H5', 2, set()),
        ('D', 'H6', 2, set()),
        ('D', 'H7', 3, {'H6'}),
    ]
    result = defaultdict(list) # src => [(dst, cost, blockers)]
    for src, dst, cost, blockers in table:
        for i in range(1, n + 1):
            result[src + str(i)].append((
                dst, cost + i - 1,
                blockers | {src + str(j) for j in range(1, i)}))
    for src, moves in list(result.items()):
        for (dst, cost, blockers) in moves:
            result[dst].append((src, cost, blockers))
    return result

TABLE = generate_lookup_table(len(state) // 4)

def generate_heuristics():
    result = {}
    for kind in 'ABCD':
        e = kind + '1'
        m = 10 ** 'ABCD'.index(kind)
        for pos, moves in TABLE.items():
            if pos[0] == kind:
                h = 0
            elif pos[0] == 'H':
                h = min(m[1] for m in moves if m[0] == e)
            else:
                h = min(a[1] + b[1] for a in TABLE[pos] for b in TABLE[e] if a[0] == b[0])
            result[(kind, pos)] = h * m
    return result

HEURISTICS = generate_heuristics()

# def show(state):
#     state = dict(state)
#     fmt = '''#############\n#%s%s.%s.%s.%s.%s%s#\n###%s#%s#%s#%s###\n  #%s#%s#%s#%s#\n  #########\n'''
#     keys = ['H1','H2','H3','H4','H5','H6','H7','A1','B1','C1','D1','A2','B2','C2','D2']
#     print(fmt % tuple(state.get(k, '.') for k in keys))

def generate_moves(state):
    result = []
    blocked = {x[0] for x in state}
    blocked_rooms = {pos[0] for pos, kind in state if pos[0] != kind and pos[0] != 'H'}
    for src, kind in state:
        m = 10 ** 'ABCD'.index(kind)
        for dst, cost, blockers in TABLE[src]:
            if dst[0] != 'H':
                if dst[0] != kind or kind in blocked_rooms:
                    continue
            if dst in blocked or blockers & blocked:
                continue
            result.append((cost * m, src, dst))
    return result

def do_move(state, move):
    _, src, dst = move
    return tuple(sorted((dst, kind) if pos == src else (pos, kind)
        for pos, kind in state))

def heuristic(state):
    return sum(HEURISTICS[(kind, pos)] for pos, kind in state)

def shortest_path(src, dst):
    seen = set()
    queue = [(heuristic(src), 0, src)]
    while queue:
        _, cost, state = heapq.heappop(queue)
        if state == dst:
            return cost
        if state in seen:
            continue
        seen.add(state)
        for move in generate_moves(state):
            new_state = do_move(state, move)
            if new_state in seen:
                continue
            new_cost = cost + move[0]
            heapq.heappush(queue,
                (new_cost + heuristic(new_state), new_cost, new_state))

print(shortest_path(state, solved))

'''
#############
#12.3.4.5.67# < H
###1#1#1#1###
  #2#2#2#2#
  #########
   ^ ^ ^ ^
   A B C D
'''
