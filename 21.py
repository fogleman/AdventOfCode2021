from itertools import *
import fileinput
import re

starting_positions = list(map(int, re.findall(r'\d+',
    ''.join(fileinput.input()))[1::2]))

def part1():
    positions = list(starting_positions)
    scores = [0] * len(positions)
    die = cycle(range(1, 101))
    turn = rolls = 0
    while True:
        step = next(die) + next(die) + next(die)
        rolls += 3
        positions[turn] = (positions[turn] + step - 1) % 10 + 1
        scores[turn] += positions[turn]
        if scores[turn] >= 1000:
            return rolls * min(scores)
        turn = (turn + 1) % len(positions)

rolls = [sum(x) for x in product([1, 2, 3], repeat=3)]

def _part2(state, memo):
    if state in memo:
        return memo[state]
    positions, scores, turn = state
    if scores[0] >= 21:
        return (1, 0)
    if scores[1] >= 21:
        return (0, 1)
    wins = [0, 0]
    for r in rolls:
        new_positions = list(positions)
        new_scores = list(scores)
        new_positions[turn] += r
        if new_positions[turn] > 10:
            new_positions[turn] -= 10
        new_scores[turn] += new_positions[turn]
        new_state = (tuple(new_positions), tuple(new_scores), (turn + 1) % 2)
        new_wins = _part2(new_state, memo)
        wins[0] += new_wins[0]
        wins[1] += new_wins[1]
    memo[state] = wins
    return wins

def part2():
    state = (tuple(starting_positions), (0, 0), 0)
    return max(_part2(state, {}))

print(part1())
print(part2())
