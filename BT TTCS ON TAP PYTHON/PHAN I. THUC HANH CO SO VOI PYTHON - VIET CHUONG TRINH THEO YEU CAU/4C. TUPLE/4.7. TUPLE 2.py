a, b = input(), input()
x = a.split(",")
y = b.split(",")
x1 = tuple([int(p) for p in x])
x2 = tuple([int(p) for p in y])

for i in range(len(x2) - 1): print(x2[i], end=",")
print(x2[-1])

for i in range(len(x1) - 1): print(x1[i], end=",")
print(x1[-1])

