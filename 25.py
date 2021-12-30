import fileinput
import numpy as np

a = np.array([list(map(int, line)) for line in
    ''.join(fileinput.input()).translate(str.maketrans('.>v', '012')).split()])

def step(a):
    for i in range(2):
        axis, code = [1, 0][i], [1, 2][i]
        e = np.roll(a, 1, axis=axis)
        w = np.roll(a, -1, axis=axis)
        b = a.copy()
        b[(a == 0) & (e == code)] = code
        b[(a == code) & (w == 0)] = 0
        a = b
    return a

def run(a):
    i = 0
    while True:
        b = step(a)
        i += 1
        if np.array_equal(a, b):
            return i
        a = b

print(run(a))
