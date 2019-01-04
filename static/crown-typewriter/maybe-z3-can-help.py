# inspiration: https://yurichev.com/blog/cabling_Z3/

from z3 import *
from string import uppercase
import json

uppercase = 'ABCDEF'

def Difference(x, y):
    return If(x < y, y - x, x - y)

with open('digraphs.json') as f:
    digraphs = json.load(f)

s = Optimize()
alphabet = {}
for c in uppercase:
    X = Int(c)
    alphabet[c] = X
    s.add(And(X >= 0, X < len(uppercase)))

s.add(Distinct(*alphabet.values()))

cost = 0
for c1 in uppercase:
    for c2 in uppercase:
        cost = cost + digraphs[c1 + c2] * Difference(alphabet[c1], alphabet[c2])

s.minimize(cost)

print "Solving..."
print s.check()
m = s.model()
out = [''] * len(uppercase)
for c in uppercase:
    out[m.evaluate(alphabet[c]).as_long()] = c

print ''.join(out)
print 'Cost:', m.evaluate(cost)
