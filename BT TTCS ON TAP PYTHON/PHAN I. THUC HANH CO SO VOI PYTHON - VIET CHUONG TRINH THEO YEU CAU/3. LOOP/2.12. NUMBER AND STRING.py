def check(s):
    for i in range (0, len(s)//2 + 1):
        if s[i] != s[len(s) - i - 1]: return False 
    return True 
m, n = int(input()), int(input())
for i in range(m, n + 1):
    if check(str(i)): print(i)