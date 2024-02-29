from math import *
def lcm(a, b):
    return a * b //gcd(a, b)
a, b = int(input()), int(input())
x1 = gcd(a, b)
x = x1
a1 = [1]
for i in range(2, int(sqrt(x))):
    if x % i == 0:
        while x % i == 0: x//=i
        a1.append(i)
if x!=1: a1.append(x)
for y in a1: print(y, end = " ")   
print()
print(x1)
print(lcm(a, b))