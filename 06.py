import fileinput

line = fileinput.input().readline()
counts = [line.count(str(i)) for i in range(10)]

def step(counts):
    result = [0] * 9
    result[6] = result[8] = counts[0]
    for i in range(8):
        result[i] += counts[i + 1]
    return result

def run(counts, n):
    for _ in range(n):
        counts = step(counts)
    return sum(counts)

print(run(counts, 80))
print(run(counts, 256))
