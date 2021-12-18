import fileinput
import math

class Node:
    def __init__(self, x, depth=0):
        self.depth = depth
        if isinstance(x, list):
            self.L = Node(x[0], depth + 1)
            self.R = Node(x[1], depth + 1)
            self.leaf = False
        else:
            self.prev = self.next = None
            self.value = x
            self.leaf = True
    def visit(self):
        yield self
        if not self.leaf:
            yield from self.L.visit()
            yield from self.R.visit()
    def magnitude(self):
        if self.leaf:
            return self.value
        return 3 * self.L.magnitude() + 2 * self.R.magnitude()
    def __repr__(self):
        if self.leaf:
            return str(self.value)
        else:
            return '[%r,%r]' % (self.L, self.R)

def build(s):
    root = Node(eval(s))
    leafs = [x for x in root.visit() if x.leaf]
    for a, b in zip(leafs, leafs[1:]):
        a.next = b
        b.prev = a
    return root

def add(a, b):
    return build('[%r,%r]' % (a, b))

def explode(node):
    if node.L.prev:
        node.L.prev.value += node.L.value
    if node.R.next:
        node.R.next.value += node.R.value
    node.leaf = True
    node.value = 0

def split(node):
    a = int(math.floor(node.value / 2))
    b = int(math.ceil(node.value / 2))
    n = Node([a, b], node.depth)
    node.leaf = False
    node.L = n.L
    node.R = n.R

def process(root):
    for node in root.visit():
        if node.depth >= 4 and not node.leaf:
            explode(node)
            return False
    for node in root.visit():
        if node.leaf and node.value > 9:
            split(node)
            return False
    return True

def reduce(root):
    while True:
        root = build(repr(root))
        if process(root):
            return root

numbers = [build(x) for x in fileinput.input()]

node = numbers[0]
for number in numbers[1:]:
    node = reduce(add(node, number))
print(node.magnitude())

hi = 0
for a in numbers:
    for b in numbers:
        hi = max(hi, reduce(add(a, b)).magnitude())
print(hi)
