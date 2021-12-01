import fileinput

def increases(values):
    return sum(b > a for a, b in zip(values, values[1:]))

values = list(map(int, fileinput.input()))
print(increases(values))

windows = [sum(values[i:i+3]) for i in range(len(values) - 2)]
print(increases(windows))
