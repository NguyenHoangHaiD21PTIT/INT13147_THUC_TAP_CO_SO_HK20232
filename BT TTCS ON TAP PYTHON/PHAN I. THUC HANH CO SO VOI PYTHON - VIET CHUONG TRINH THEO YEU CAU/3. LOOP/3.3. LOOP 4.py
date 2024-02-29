from sys import stdin
a = []
for line in stdin: a.append(int(line))
for i in range (len(a) - 1, -1, -1): print(a[i], end = " ")
print()
for x in a: 
    if x > 150: continue
    if x > 500: break
    if x%5==0: print(x, end = " ")