from sys import stdin
a = []
for line in stdin: a.append(int(line))
b = [x * x for x in a]
for x in b: print(x, end = " ")