from sys import stdin
d = dict()
for line in stdin:
    x = line.strip().split()
    d[x[0] + x[1]] = x[2]
a = list(d.items())
for y in a: print(y[0], y[1])