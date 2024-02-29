from sys import stdin
a = []
for line in stdin: a.append(line.strip())
x = len(a)//2 
for i in range(x): print(a[i] + a[i + x], end = " ")
    