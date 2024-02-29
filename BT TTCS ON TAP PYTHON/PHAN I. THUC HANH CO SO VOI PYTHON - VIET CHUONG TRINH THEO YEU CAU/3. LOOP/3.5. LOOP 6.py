s = input()
print("1. ", end = "")
for x in s:
    if x.isdigit(): print(x, end = "")
print()

a = s.split("-")
print("2. ", end = "")
for x in a:
    tmp = ""
    for y in x: 
        if y.isalpha() or y.isdigit(): tmp+=y 
    if tmp!="": print(tmp, end = " ")
print()

print("3. ", end = "")
for x in a: print(x.strip(), end = " ")
