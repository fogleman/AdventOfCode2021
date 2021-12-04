import fileinput
import numpy as np

def run(sequence, boards, last):
    seen = set()
    done = set()
    for x in sequence:
        seen.add(x)
        for i, board in enumerate(boards):
            if any(set(row) <= seen for row in list(board) + list(board.T)):
                done.add(i)
                if not last or len(done) == len(boards):
                    return sum(set(board.flatten()) - seen) * x

lines = list(filter(None, [list(map(int, x.replace(',', ' ').split()))
    for x in fileinput.input()]))
sequence, boards = lines.pop(0), np.split(np.array(lines), len(lines) // 5)

print(run(sequence, boards, 0))
print(run(sequence, boards, 1))
