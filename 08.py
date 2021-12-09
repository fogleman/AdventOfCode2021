import fileinput

from itertools import *

entries = [(x.split()[:10], x.split()[-4:]) for x in fileinput.input()]

print(sum(len(x) in [2, 3, 4, 7] for e in entries for x in e[1]))

def solve(patterns, outputs):
    nums = [
        'abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf',
        'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
    for p in permutations('abcdefg'):
        def convert(x):
            return ''.join(sorted(chr(ord('a') + p.index(c)) for c in x))
        if all(convert(x) in nums for x in patterns):
            return int(''.join(str(nums.index(convert(x))) for x in outputs))

print(sum(solve(*e) for e in entries))
