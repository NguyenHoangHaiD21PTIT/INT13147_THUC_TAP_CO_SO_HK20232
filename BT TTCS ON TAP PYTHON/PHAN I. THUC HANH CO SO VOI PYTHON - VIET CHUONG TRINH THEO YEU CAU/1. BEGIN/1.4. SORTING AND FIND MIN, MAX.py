a, b, c = int(input()), int(input()), int(input())
A = []
A.append(a); A.append(b); A.append(c); 
A.sort() 
print(A[0])
for x in A: print(x, end = " ")