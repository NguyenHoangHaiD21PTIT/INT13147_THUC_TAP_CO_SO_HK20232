from sys import stdin
d = dict()
a = []
for line in stdin: a.append(line.strip())
for i in range (len(a) - 1):
    x = a[i].split(":")
    if len(x) == 2: d[x[0]] = x[1]
print(a[-1] + ":" + d[a[-1]])
