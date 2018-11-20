import random
import string
import json
import itertools

f = open('digraphs.json', 'r')
digraphs = json.load(f)
f.close()

def cost(perm):
    total = 0
    for a, b in itertools.product(string.uppercase, string.uppercase):
        total += abs(perm.index(a) - perm.index(b)) * digraphs[a+b]
    return total

def swap(text, i, j):
    if i == j:
        return text
    if i > j:
        return swap(text, j, i)
    return text[:i] + text[j] + text[i + 1:j] + text[i] + text[j + 1:]

def update(current_perm, current_cost):
    for i, j in itertools.product(xrange(26), xrange(26)):
        new_perm = swap(current_perm, i, j)
        new_cost = cost(new_perm)
        if new_cost < current_cost:
            return (new_perm, new_cost)
    return (current_perm, current_cost)

CROWN = 'XQKGBPMCOFLANDTHERISUWYJVZ'
print cost(CROWN)

BEST = 'ZKVGWCDNIAHTESROMLUFYBPJXQ'
print cost(BEST)

def shuffle(s):
    l = list(s)
    random.shuffle(l)
    return ''.join(l)

current_perm = shuffle(string.uppercase)
current_cost = cost(current_perm)

while True:
    print current_perm, current_cost
    current_perm, current_cost = update(current_perm, current_cost)
