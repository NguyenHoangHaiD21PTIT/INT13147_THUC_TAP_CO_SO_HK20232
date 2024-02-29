from sys import stdin
a = []
print("1.", end = " ")
for line in stdin:
    x = (len(line) - 4)//2
    print(line[x: x + 4:], end = " ")
    a.append(line.strip())
print()

print("2. ", end = "")
pos = len(a[0])//2
print(a[0][:pos:] + a[1] + a[0][pos::])

print("3. ", end = "")
for x in a: print(x[0], end = "")
for x in a: print(x[-1], end = "")
print()

print("4. ", end = "")
for x in a:
    thuong = []; hoa = []; so = []; kiTu = [];
    for y in x:
        if y.islower(): thuong.append(y)
        elif y.isupper(): hoa.append(y)
        elif y.isdigit(): so.append(y)
        else: kiTu.append(y)
    for x in thuong: print(x, end = "")
    for x in hoa: print(x, end = "")
    for x in so: print(x, end = "")
    for x in kiTu: print(x, end = "")
    print(" ", end = "")
print()
  
print("5. ", end = "")
for x in a:
    chu, so, kiTu = 0, 0, 0 
    for y in x: 
        if y.isalpha(): chu+=1 
        elif y.isdigit(): so+=1
        else: kiTu+=1
    print(chu, so, kiTu, end = " ")