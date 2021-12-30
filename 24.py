from collections import *
from itertools import *
import fileinput

program = [tuple(int(x) if x[-1].isdigit() else x
    for x in line.strip().split()) for line in fileinput.input()]

programs = [tuple(g) for k, g in
    groupby(program, lambda x: x[0] == 'inp') if not k]

def run_program(program, w, z):
    d = dict(w=w, x=0, y=0, z=z)
    for op, a, b in program:
        b = d.get(b, b)
        if op == 'add':
            d[a] += b
        elif op == 'mul':
            d[a] *= b
        elif op == 'div':
            d[a] //= b
        elif op == 'mod':
            d[a] %= b
        elif op == 'eql':
            d[a] = int(d[a] == b)
    return d['z']

def search(programs, order, seq, memos, z):
    i = len(seq)
    if i >= len(programs):
        if z == 0:
            return ''.join(map(str, seq))
        return
    if z in memos[i]:
        return
    memos[i].add(z)
    for w in order:
        nz = run_program(programs[i], w, z)
        seq.append(w)
        result = search(programs, order, seq, memos, nz)
        seq.pop()
        if result:
            return result

print(search(programs, list(range(9, 0, -1)), [], defaultdict(set), 0))
print(search(programs, list(range(1, 10)), [], defaultdict(set), 0))
