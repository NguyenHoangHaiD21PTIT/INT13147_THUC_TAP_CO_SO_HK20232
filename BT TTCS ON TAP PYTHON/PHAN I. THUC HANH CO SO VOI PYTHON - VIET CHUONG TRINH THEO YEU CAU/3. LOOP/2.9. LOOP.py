from math import *
def check_prime(n):
    if n <=1: return False
    for i in range (2, int(sqrt(n)) + 1):
        if n % i ==0: return False 
    return True 

n = int(input())
n-=1
print(n * (n + 1)//2)
print(factorial(n))
s = 0
for i in range (1, n + 1): s+=1.0/i 
print("{:.2f}".format(s))
n+=1
if check_prime(n): print("Prime")
else: print("Not a prime")