def sum(x):
    if x ==1: return 1
    return x + sum(x - 1)

print(sum(int(input())))