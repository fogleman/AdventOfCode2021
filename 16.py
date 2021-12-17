from functools import reduce
from io import StringIO
import fileinput
import operator

data = ''.join(fileinput.input()).strip()

def hex_bits(data):
    bits = bin(int(data, 16))[2:]
    return '0' * (len(data) * 4 - len(bits)) + bits

def read(s, n):
    return int(s.read(n), 2)

class Packet:
    def __init__(self, version, type_id, literal=None, children=None):
        self.version = version
        self.type_id = type_id
        self.literal = literal
        self.children = children or []
    def version_sum(self):
        return self.version + sum(x.version_sum() for x in self.children)
    def value(self):
        values = [x.value() for x in self.children]
        if self.type_id == 0:
            return sum(values)
        if self.type_id == 1:
            return reduce(operator.mul, values)
        if self.type_id == 2:
            return min(values)
        if self.type_id == 3:
            return max(values)
        if self.type_id == 4:
            return self.literal
        if self.type_id == 5:
            return int(values[0] > values[1])
        if self.type_id == 6:
            return int(values[0] < values[1])
        if self.type_id == 7:
            return int(values[0] == values[1])
    def __repr__(self):
        rows = []
        if self.literal is None:
            rows.append('version=%d, type_id=%d' % (self.version, self.type_id))
        else:
            rows.append('version=%d, type_id=%d, literal=%d' % (self.version, self.type_id, self.literal))
        for child in self.children:
            for line in repr(child).split('\n'):
                rows.append('  ' + line)
        return '\n'.join(rows)

def parse_literal(s):
    literal = 0
    while True:
        more = read(s, 1)
        literal = (literal << 4) | read(s, 4)
        if not more:
            return literal

def parse_packets(s):
    packets = []
    while True:
        try:
            packets.append(parse_packet(s))
        except Exception:
            return packets

def parse_packet(s):
    version, type_id = read(s, 3), read(s, 3)
    if type_id == 4:
        return Packet(version, type_id, literal=parse_literal(s))
    if read(s, 1) == 0:
        children = parse_packets(StringIO(s.read(read(s, 15))))
    else:
        children = [parse_packet(s) for _ in range(read(s, 11))]
    return Packet(version, type_id, children=children)

p = parse_packet(StringIO(hex_bits(data)))
print(p.version_sum())
print(p.value())
