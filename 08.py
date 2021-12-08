import fileinput

from itertools import permutations

entries = [(line.split()[:10], line.split()[-4:])
    for line in fileinput.input()]

print(sum(len(x) in [2, 3, 4, 7] for e in entries for x in e[1]))

def solve(patterns, outputs):
    numbers = [
        'abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf',
        'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg',
    ]
    for m in [dict(zip('abcdefg', p)) for p in permutations('abcdefg')]:
        convert = lambda x: ''.join(sorted(m[c] for c in x))
        if {convert(x) for x in patterns} != set(numbers):
            continue
        return int(''.join(str(numbers.index(convert(x))) for x in outputs))

print(sum(solve(*e) for e in entries))
