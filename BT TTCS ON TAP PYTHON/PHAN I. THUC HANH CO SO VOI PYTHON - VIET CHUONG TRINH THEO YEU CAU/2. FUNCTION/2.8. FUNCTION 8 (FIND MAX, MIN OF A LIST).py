from sys import stdin
a = []
for line in stdin: a.append(int(line))
print(min(a)); print(max(a))