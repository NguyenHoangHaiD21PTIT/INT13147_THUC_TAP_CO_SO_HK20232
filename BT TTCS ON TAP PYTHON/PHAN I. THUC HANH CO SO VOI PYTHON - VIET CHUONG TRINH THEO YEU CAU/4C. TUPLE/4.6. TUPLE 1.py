a = []
for i in range(3): a.append(input())
b = a[1].strip().split(", ")
b1 = [int(b[i]) for i in range(len(b))]
c = a[2].strip().split(", ")
c1 = tuple([int(c[i]) for i in range(len(c))])
ans = (a[0], b1, c1)
print(ans)
print(ans[1][1])