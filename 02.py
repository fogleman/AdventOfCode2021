import fileinput

lines = list(fileinput.input())

x = y = 0
for line in lines:
    line = line.strip()
    d, n = line.split()
    n = int(n)
    if d == 'up':
        y -= n
    elif d == 'down':
        y += n
    else:
        x += n
print(x * y)

x = y = aim = 0
for line in lines:
    d, n = line.strip().split()
    n = int(n)
    if d == 'up':
        aim -= n
    elif d == 'down':
        aim += n
    else:
        x += n
        y += n * aim
print(x * y)
