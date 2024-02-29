def check(s):
    for i in range (0, len(s)//2 + 1):
        if s[i] != s[len(s) - i - 1]: return False 
    return True 
print(check(input()))