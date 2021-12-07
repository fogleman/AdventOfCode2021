import fileinput

crabs = list(map(int, fileinput.input().readline().split(',')))

def f(x):
    return sum(abs(x - y) for y in crabs)

def g(x):
    return sum(abs(x - y) * (abs(x - y) + 1) // 2 for y in crabs)

print(min(f(x) for x in range(min(crabs), max(crabs))))
print(min(g(x) for x in range(min(crabs), max(crabs))))
