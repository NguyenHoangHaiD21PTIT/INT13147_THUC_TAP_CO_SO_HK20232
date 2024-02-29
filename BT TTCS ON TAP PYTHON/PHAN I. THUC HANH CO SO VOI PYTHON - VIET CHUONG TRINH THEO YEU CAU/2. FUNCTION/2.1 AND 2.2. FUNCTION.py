def func1(a, b, c):
    s = a + " " + b
    if b[-1]!="?": s+="?"
    s+=" " + c.capitalize()
    print(s)
def func2(x, y):
    print(x, y)
a, b, c, x, y = input(), input(), input(), int(input()), int(input())
func1(a, b, c); func2(x, y); 