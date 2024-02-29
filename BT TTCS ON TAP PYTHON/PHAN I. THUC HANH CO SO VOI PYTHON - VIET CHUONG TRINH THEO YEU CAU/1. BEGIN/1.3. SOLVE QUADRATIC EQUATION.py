from math import *
a, b, c = int(input()), int(input()), int(input())
denta = b * b - 4 * a * c 
if denta < 0: print("The equation has no real root.")
elif denta == 0: 
    x = -b / (2.0 * a)
    print("{:.2f}".format(x) + " " + "{:.2f}".format(x))
else: 
    x1 = (-b - sqrt(denta))/(2.0 * a)
    x2 = (-b + sqrt(denta))/(2.0 * a)
    print("{:.2f}".format(x1) + " " + "{:.2f}".format(x2))