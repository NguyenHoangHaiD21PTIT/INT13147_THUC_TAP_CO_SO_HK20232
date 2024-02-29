def check(a, b):
    x, y = [], []
    for a1 in a: 
        if a1!=" ": x.append(a1)
    for b1 in b: 
        if b1!=" ": y.append(b1)
    x.sort(); y.sort();
    return x==y

a, b = input(), input()
print(check(a, b))