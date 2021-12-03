import fileinput

values = [int(line, 2) for line in fileinput.input()]

def split(values, index):
    mask = 1 << index
    zeros = []
    ones = []
    for x in values:
        if x & mask:
            ones.append(x)
        else:
            zeros.append(x)
    return zeros, ones

gamma = 0
epsilon = 0
for i in range(12):
    zeros, ones = split(values, i)
    if len(ones) > len(values) / 2:
        gamma |= 1 << i
    else:
        epsilon |= 1 << i

print(gamma * epsilon)

def search(values, less):
    for i in range(11, -1, -1):
        zeros, ones = split(values, i)
        if less:
            if len(zeros) <= len(ones):
                values = zeros
            else:
                values = ones
        else:
            if len(ones) >= len(zeros):
                values = ones
            else:
                values = zeros
        if len(values) == 1:
            return values[0]

print(search(values, 0) * search(values, 1))
